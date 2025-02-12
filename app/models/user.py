# app/models/user.py

import uuid
from datetime import datetime, timezone, timedelta
from sqlalchemy import Column, String, Boolean, DateTime, or_
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from app.core.config import get_settings
from app.database import Base
from app.models.calculation import Calculation

settings = get_settings()

class User(Base):
    __tablename__ = "users"
    
    # Use a PostgreSQL UUID primary key to match test expectations.
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True)
    # Columns expected by tests and response schemas.
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    
    # NEW: Relationship to calculations.
    # Assumes that your Calculation model defines a foreign key to users.id and
    # a relationship with back_populates="calculations".
    calculations = relationship(Calculation, back_populates="user", cascade="all, delete-orphan")
    
    def __init__(self, *args, **kwargs):
        # Allow "hashed_password" as an alias for "password".
        if "hashed_password" in kwargs:
            kwargs["password"] = kwargs.pop("hashed_password")
        super().__init__(*args, **kwargs)
    
    @property
    def hashed_password(self):
        """Return the stored hashed password."""
        return self.password

    def __str__(self):
        return f"<User(name={self.first_name} {self.last_name}, email={self.email})>"

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hash a plain-text password using the application's password hashing utility.
        """
        from app.auth.jwt import get_password_hash
        return get_password_hash(password)

    def verify_password(self, plain_password: str) -> bool:
        """
        Verify a plain-text password against this user's stored hashed password.
        """
        from app.auth.jwt import verify_password
        return verify_password(plain_password, self.password)

    @classmethod
    def register(cls, db, user_data: dict):
        """
        Register a new user.

        Validates that:
          - A password is provided and is at least 6 characters long.
          - The email or username is not already in use.
        
        Hashes the password and creates a new user instance, adding it to the session.

        Raises:
            ValueError: If the password is missing/too short or if the email/username already exists.
        """
        password = user_data.get("password")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        
        # Check for duplicate email or username.
        existing_user = db.query(cls).filter(
            or_(cls.email == user_data["email"], cls.username == user_data["username"])
        ).first()
        if existing_user:
            raise ValueError("Username or email already exists")
        
        hashed_password = cls.hash_password(password)
        user = cls(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            username=user_data["username"],
            password=hashed_password,
            is_active=True,
            is_verified=False,
            last_login=None  # created_at and updated_at are auto-set.
        )
        db.add(user)
        # Let the caller commit the transaction.
        return user


    @classmethod
    def authenticate(cls, db, username_or_email: str, password: str):
        """
        Authenticate a user by username (or email) and password.
        Returns token response data if successful, None if authentication fails.
        """
        user = db.query(cls).filter(
            or_(cls.username == username_or_email, cls.email == username_or_email)
        ).first()

        if not user or not user.verify_password(password):
            return None

        # Update the last_login timestamp
        user.last_login = datetime.now(timezone.utc)
        db.flush()

        # Create access token
        access_token = cls.create_access_token({"sub": str(user.id)})
        
        # Create refresh token
        refresh_token = cls.create_refresh_token({"sub": str(user.id)})
        
        # Calculate token expiration
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_at": expires_at,
            "user": user
        }

    @classmethod
    def create_refresh_token(cls, data: dict) -> str:
        """Create a refresh token."""
        from app.auth.jwt import create_token
        from app.schemas.token import TokenType
        return create_token(data["sub"], TokenType.REFRESH)

    @classmethod
    def create_access_token(cls, data: dict) -> str:
        """
        Create a JWT access token with the given payload.
        
        The payload must include a "sub" key containing the user's identifier.
        """
        from app.auth.jwt import create_token
        from app.schemas.token import TokenType
        return create_token(data["sub"], TokenType.ACCESS)

    @classmethod
    def verify_token(cls, token: str):
        """
        Verify a JWT token and return the user identifier if valid.
        
        Returns:
            The user ID (as a UUID) if the token is valid, or None if the token is invalid.
        """
        from app.core.config import settings
        from jose import jwt, JWTError
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
            sub = payload.get("sub")
            if sub is None:
                return None
            try:
                # Return the UUID instance.
                return uuid.UUID(sub)
            except (ValueError, TypeError):
                return sub
        except JWTError:
            return None
