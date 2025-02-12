# **Module 12: Implementing and Testing User & Calculation Routes**

## **Module Overview**

In **Module 12**, you will connect your application’s **User** and **Calculation** models to **FastAPI routes**, enabling real **BREAD operations** on calculations and **user login/registration** flows. Although you already have secure user models and a calculation schema from previous modules, this is where you’ll finally expose these resources as **RESTful endpoints**. You’ll test these routes both **manually** (using OpenAPI docs) and via **integration tests** in your **CI/CD pipeline**, ensuring your service is stable before a front-end UI is added in Module 13.

By the end of this module, you will:

1. Create **FastAPI routes** for **user login/registration** (auth flows).  
2. Implement **BREAD** endpoints (Browse, Read, Edit, Add, Delete) for your `Calculation` model.  
3. Validate requests/responses with Pydantic (e.g., `UserCreate`, `UserLogin`, `CalculationCreate`, `CalculationRead`).  
4. Write **integration tests** (using `pytest`) that confirm each route’s behavior in a Docker-based CI environment.  
5. Continue building, testing, and deploying your Docker image to Docker Hub as part of your evolving final project.

### **Relevant Course Learning Outcomes (CLOs)**

- **CLO 3:** Create Python applications with automated testing.  
- **CLO 4:** Set up GitHub Actions for Continuous Integration (CI), automating tests and Docker builds to demonstrate DevOps principles.  
- **CLO 10:** Apply containerization techniques to containerize applications using Docker.  
- **CLO 11:** Create, consume, and test REST APIs using Python.  
- **CLO 12:** Integrate Python programs with SQL databases to create and manipulate data.  
- **CLO 13:** Serialize, deserialize, and validate JSON using Python with Pydantic.  
- **CLO 14:** Utilize best practices for software development security by implementing secure authentication and authorization techniques, including encryption, hashing, and encoding.

---

## **Why Focus on User & Calculation Routes Now?**

1. **Complete the Server Logic:** Modules 10 and 11 gave you user and calculation models; now you’ll create the **routes** to actually manipulate this data.  
2. **Foundational for Next Steps:** With endpoints in place, Module 13 can introduce a front-end or advanced testing frameworks on top of a stable, tested back-end.  
3. **Incremental Development:** Testing endpoints thoroughly with `pytest` and OpenAPI ensures you have reliable REST APIs before layering UI interactions.

---

## **Module 12 Outline**

1. **User Routes**  
   - **Register** (signup) endpoint: Accepts `UserCreate` data, hashes passwords, and stores new users.  
   - **Login** endpoint: Authenticates a user by verifying password hashes, potentially returning a session token (optional advanced feature).  
   - Additional optional user endpoints if you want to handle update, delete, etc.

2. **Calculation Routes**  
   - **Browse**: `GET /calculations` lists all.  
   - **Read**: `GET /calculations/{id}` returns a single calculation.  
   - **Edit**: `PUT`/`PATCH /calculations/{id}` updates a record.  
   - **Add**: `POST /calculations` creates a new calculation (Add, Sub, Multiply, Divide).  
   - **Delete**: `DELETE /calculations/{id}` removes a record.

3. **Manual Testing with OpenAPI**  
   - Explore the generated docs (e.g., `/docs` or `/redoc`).  
   - Manually test each endpoint (user registration, login, calculation creation, etc.) for correct responses and data handling.

4. **Integration Testing with Pytest**  
   - Spin up a **PostgreSQL** container in GitHub Actions.  
   - Test user endpoints (register + login).  
   - Test each calculation endpoint (BREAD).  
   - Validate status codes, JSON responses, DB changes.

5. **CI/CD Continuation**  
   - Keep your pipeline from prior modules, ensuring successful tests -> Docker Hub deployment.  
   - This sets the stage for a front-end interface in Module 13.

---

## **Hands-On Assignment**

**Title:** User & Calculation Routes + Integration Testing  
**Grading Type:** Points  

### **Instructions:**

1. **Implement User Endpoints**  
   - **Register** (`POST /users/register`) using `UserCreate`.  
   - **Login** (`POST /users/login`) verifying hashed passwords.  
   - Optionally track user sessions/tokens if you wish to restrict certain endpoints to authenticated users.

2. **Implement Calculation Endpoints (BREAD)**  
   - **Browse** (`GET /calculations`)  
   - **Read** (`GET /calculations/{id}`)  
   - **Edit** (`PUT` or `PATCH /calculations/{id}`)  
   - **Add** (`POST /calculations`)  
   - **Delete** (`DELETE /calculations/{id}`)  
   - Use your existing `CalculationCreate`, `CalculationRead` schemas and underlying SQLAlchemy model.

3. **Test Manually + OpenAPI**  
   - Access `/docs` or `/redoc` on your FastAPI server.  
   - Confirm endpoints accept/return the correct data.

4. **Write Integration Tests (pytest)**  
   - **GitHub Actions**: Spin up Postgres as before.  
   - **User Tests**: Register, login, verify data in DB.  
   - **Calculation Tests**:  
     - Create a new calculation, retrieve it, update it, delete it.  
     - Confirm invalid data triggers errors (status codes, error responses).

5. **Maintain CI/CD**  
   - All tests (user + calculation) run automatically on each commit.  
   - A successful run pushes a new Docker image to Docker Hub.

6. **Submit**  
   - **GitHub Repository Link** (with your own code):  
     - In **README**, detail how to run integration tests + do manual checks via OpenAPI.  
     - Link to your Docker Hub repository.  
   - This module completes your back-end logic; you’ll add a front-end in Module 13.
# **Grading Expectations**

Your submissions for the **Hands-On Assignment** will be evaluated based on the following two criteria:

### **1. Submission Completeness (50 Points)**

- **GitHub Repository Link:**
  - Provided and accessible.
  - Contains all necessary files (`User` and `Calculation` routes, tests, GitHub Actions workflow).

- **Screenshots:**
  - **GitHub Actions Workflow:** Screenshot showing a successful run of the GitHub Actions workflow.
  - **Application Running in Browser:** Screenshot demonstrating user registration/login and calculation endpoints operational.

- **Documentation:**
  - Includes a reflection document addressing key experiences and challenges faced during the development and deployment process.
  - README file contains instructions on how to run tests locally and links to the Docker Hub repository.

### **2. Functionality of User & Calculation Routes and CI/CD Pipeline (50 Points)**

- **User Routes:**
  - **Register** and **Login** endpoints implemented correctly with Pydantic validation and secure password handling.
  
- **Calculation Routes (BREAD):**
  - **Browse**, **Read**, **Edit**, **Add**, and **Delete** endpoints implemented correctly.
  - Proper validation of requests and responses using Pydantic schemas.

- **Testing and CI/CD:**
  - Comprehensive integration tests for user and calculation routes are written and pass successfully in the GitHub Actions workflow.
  - CI/CD pipeline is properly configured to build, test, and deploy the Docker image to Docker Hub without errors.
  - Docker image is functional and can be pulled from Docker Hub, running the application as expected.

---
**Total: 100 Points**
---

## **Reflect**

**Title:** Module 12 Reflection  
**Grading Type:** Points  

**Instructions (600–700 words)**:

1. **RESTful Endpoints (CLO 11)**: How did implementing user login/registration and calculation routes integrate with your existing models?  
2. **Testing & CI (CLO 3 & 4)**: Discuss how integration testing with `pytest` and Docker ensures your endpoints remain reliable.  
3. **DB Integration (CLO 12 & 13)**: Reflect on how your Pydantic schemas and database logic from Modules 10–11 translated into route-level functionality.  
4. **Security & Best Practices (CLO 14)**: Note any security measures (e.g., verifying user ownership, hashing checks) that protect these endpoints.

---

## **Quiz**

**Title:** User & Calculation Routes Quiz  
**Grading Type:** Points  

### **Instructions:**

1. **Complete the Quiz on Canvas**, covering:

   - Designing user registration/login routes.  
   - BREAD endpoints for the calculation model.  
   - Manual testing with `/docs`, integration testing with a DB.  
   - Docker-based CI workflow.

2. **Question Types:**  
   - **Multiple-Choice:** Identify correct route definitions or best practices for data validation.  
   - **Short Answer:** Summarize how you handle user auth or a failing calculation test scenario.

---

## **Tips for Success**

1. **Keep Routes Focused**: Stick to user auth endpoints + BREAD for calculations. No front-end complexity yet.  
2. **Test Thoroughly**: Combine manual checks via OpenAPI with automated integration tests to guarantee correctness.  
3. **Security**: If you attach calculations to specific users, ensure you only allow the owner to modify them.  
4. **CI/CD**: Continue the same pipeline approach—your container should now serve tested endpoints.  
5. **Document**: This code forms the core back-end for your final project; maintain clarity for future expansions.

---

## **Submission Deadline**

Provide the following by **[Insert Deadline Here]**:

1. **GitHub Repo Link**: With user & calculation routes, tests, and updated CI config.  
2. **Module 12 Reflection** (600–700 words).  
3. **README** showing Docker Hub link and test instructions (manual + pytest).

Late submissions may face course policy penalties.

---

**Excellent Work!** You now have a functional **back-end** with **user login/registration** and fully tested **calculation routes**—ready for a front-end interface in Module 13. By ensuring each endpoint is well-tested and secure, you lay the foundation for a truly production-ready web application.
