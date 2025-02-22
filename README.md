# **Module 13: JWT Login & Registration with Front-End and Playwright Tests**

## **Module Overview**

In **Module 13**, you will **focus specifically** on **user authentication** by creating a minimal **JWT-based** login and registration flow—**without** tackling the full BREAD functionality for calculations (that’s coming in **Module 14**). This module will have you build a **simple front-end** (HTML/CSS/JS) for **login and registration**, add **client-side validation**, and create **Playwright** tests to verify both **positive** (valid inputs) and **negative** (invalid data) scenarios in a **Docker-based CI/CD** pipeline.

By the end of this module, you will:

1. Implement **JWT login** (returning a token for valid credentials).  
2. Implement **JWT registration** (creating a new user, returning a token or confirmation).  
3. Build basic **front-end pages** for login and registration, with **client-side validation**.  
4. Write **Playwright** end-to-end tests covering success (valid registration/login) and failure (invalid data, wrong credentials).  
5. Continue using **Docker** and **GitHub Actions** to automate tests, pushing an updated image to Docker Hub if all tests pass.

### **Relevant Course Learning Outcomes (CLOs)**

- **CLO 3:** Create Python applications with automated testing.  
- **CLO 4:** Set up GitHub Actions for Continuous Integration (CI), automating tests and Docker builds to demonstrate DevOps principles.  
- **CLO 10:** Apply containerization techniques to containerize applications using Docker.  
- **CLO 11:** Create, consume, and test REST APIs using Python.  
- **CLO 12:** Integrate Python programs with SQL databases to create and manipulate data.  
- **CLO 13:** Serialize, deserialize, and validate JSON using Python with Pydantic.  
- **CLO 14:** Utilize best practices for software development security by implementing secure authentication and authorization techniques, including encryption, hashing, and encoding.

---

## **Why Focus on JWT Login & Registration Now?**

1. **Incremental Development**: You already have user models and routes from previous modules—now you’ll concentrate solely on **secure authentication** before adding the full BREAD for calculations in Module 14.  
2. **User-Centric UX**: A minimal front-end for registration/login clarifies how real users (or clients) interact with your secure system.  
3. **Testing Confidence**: End-to-end (E2E) tests with **Playwright** confirm that the entire login/registration workflow functions as expected under various input conditions.

---

## **Module 13 Outline**

1. **JWT-Based Registration and Login**  
   - **/register** (or `/users/register`): Accepts new user data, returns a JWT or success message upon valid input.  
   - **/login** (or `/users/login`): Checks credentials, returns a JWT upon success, or an error code upon failure.  
   - Minimal token logic (e.g., `pyjwt`) to sign user ID/username, maybe with a short expiration.

2. **Front-End Pages**  
   - **register.html** (or integrated in `index.html`): A form prompting user info, including **basic validations** (email format, password length).  
   - **login.html**: A form for email/password login, again with client-side checks.  
   - On success, store the JWT (e.g., `localStorage`) for future requests, or just confirm success if you’re not implementing further routes yet.

3. **Client-Side Validation & Basic Security**  
   - Email format checks (simple regex or `type="email"`).  
   - Password length checks.  
   - Possibly sanitize or carefully handle user-provided data to avoid trivial XSS in the front-end.

4. **Playwright E2E Testing**  
   - **Positive Tests**:  
     1. **Valid Registration**: Provide correct email/password meeting min length -> success message, user created.  
     2. **Valid Login**: Provide correct credentials -> server returns JWT, front-end indicates success or stores token.  
   - **Negative Tests**:  
     1. **Short Password** or invalid email -> front-end shows error, server route not called or returns 400.  
     2. **Wrong Credentials** -> server returns 401, front-end shows “invalid login” message.  
   - Ensure each test asserts UI elements change accordingly (e.g., an error message div, or a success message).

5. **Maintaining CI/CD**  
   - In GitHub Actions:  
     - Install and run **Playwright**.  
     - Spin up your back-end + DB container.  
     - Execute E2E tests. If they pass, push new Docker image to Docker Hub.

---

## **Hands-On Assignment**

**Title:** JWT Login/Registration with Client-Side Validation & Playwright E2E  
**Grading Type:** Points  

### **Instructions (Detailed)**:

1. **JWT Login & Registration Routes**  
   - **/register**:  
     - Receives user info (username/email, password).  
     - Validates (check duplicates, hash password, store in DB).  
     - Returns a JWT or success response.  
   - **/login**:  
     - Valid credentials -> return JWT.  
     - Invalid -> 401 Unauthorized.

2. **Front-End Pages**  
   - **register.html**:  
     - Fields for email, password, (optional) confirm password.  
     - **Client-side** checks (email format, min password length).  
     - On success (server responds 200/201), display success or store the JWT.  
   - **login.html**:  
     - Fields for email, password.  
     - Client-side checks, minimal.  
     - On success, store the JWT or display a success message.

3. **Playwright E2E Tests**  
   - **Positive**:  
     1. Register with valid data (e.g., email format, pass length), confirm success message.  
     2. Login with correct credentials, confirm success or token stored.  
   - **Negative**:  
     1. Register with short password -> front-end error or 400 from server, verify UI shows error.  
     2. Login with wrong password -> server returns 401, UI shows invalid credentials message.  
   - Ensure tests locate form fields, type invalid/valid data, submit, and check resulting UI states or server responses.

4. **CI/CD**  
   - Retain your Docker-based pipeline from prior modules.  
   - On each commit:  
     - GitHub Actions spins up DB + server.  
     - Runs Playwright tests.  
     - If all pass, push image to Docker Hub.

5. **Submit**  
   - **GitHub Repo Link** with your own code (JWT routes, front-end forms, E2E tests).  
   - **README**: Provide instructions for running front-end, E2E tests, and link to your Docker Hub repo.  
   - Next module (Module 14) will add the full BREAD for calculations to the front-end.
# **Grading Expectations**

Your submissions for the **Hands-On Assignment** will be evaluated based on the following two criteria:

### **1. Submission Completeness (50 Points)**

- **GitHub Repository Link:**
  - Provided and accessible.
  - Contains all necessary files (`JWT` authentication routes, front-end code, Playwright tests, GitHub Actions workflow).

- **Screenshots:**
  - **GitHub Actions Workflow:** Screenshot showing a successful run of the GitHub Actions workflow.
  - **Playwright E2E Tests:** Screenshot demonstrating Playwright tests passing.
  - **Front-End Application:** Screenshot of the login and registration pages functioning correctly.

- **Documentation:**
  - Includes a reflection document addressing key experiences and challenges faced during the development and testing process.
  - README file contains instructions on how to run the front-end, execute Playwright tests, and links to the Docker Hub repository.

### **2. Functionality of JWT Authentication and CI/CD Pipeline (50 Points)**

- **JWT Authentication:**
  - **Registration Endpoint:** `/register` correctly accepts user data, hashes passwords, and stores new users.
  - **Login Endpoint:** `/login` authenticates users by verifying hashed passwords and returns a JWT upon successful login.
  - **Pydantic Validation:** User data is validated using Pydantic schemas to ensure data integrity and security.

- **Front-End Integration:**
  - **Login and Registration Pages:** Functional HTML/CSS/JS pages with client-side validation for email formats and password requirements.
  - **Token Handling:** JWT tokens are correctly stored (e.g., in `localStorage`) and used for authenticated requests.

- **Playwright E2E Tests:**
  - **Positive Tests:** Successful user registration and login with valid inputs.
  - **Negative Tests:** Proper handling of invalid inputs, such as short passwords or incorrect login credentials, with appropriate UI feedback.

- **CI/CD Pipeline:**
  - **Automated Testing:** Playwright E2E tests run successfully in the GitHub Actions workflow.
  - **Docker Hub Deployment:** Docker image is built and pushed to Docker Hub automatically upon passing all tests.

---

**Total: 100 Points**
---

## **Reflect**

**Title:** Module 13 Reflection  
**Grading Type:** Points  
**Instructions (300–500 words)**:

1. **Front-End Integration**: How did adding a JWT-based login/registration flow (with client-side validation) deepen your full-stack perspective?  
2. **DevOps & Testing**: Discuss the role of Playwright E2E tests in verifying login/registration flows, especially for both valid/invalid scenarios.  
3. **Security & Best Practices**: Which client-side checks (password length/email format) and JWT token storage strategies did you employ, and how do these complement server-side security?

4. **Challenges & Solutions**: Summarize any difficulties (JWT generation/verification, storing tokens, Docker environment for E2E) and how you overcame them.

---

## **Quiz**

**Title:** JWT Login & Registration, Front-End Validation, Playwright E2E Quiz  
**Grading Type:** Points  

### **Instructions:**

1. **Complete the Quiz on Canvas**, covering:

   - Minimal JWT flow in FastAPI (login/register).  
   - Client-side validation for basic input fields.  
   - Positive/negative test scenarios with Playwright.  
   - Docker-based CI integration for E2E tests.

2. **Question Types:**  
   - **Multiple-Choice**: Identify correct/incorrect approaches to JWT usage or front-end validations.  
   - **Short Answer**: Summarize how to handle a short password case or invalid login credentials in E2E.

---

## **Tips for Success**

1. **Focus on Simplicity**: A single JWT with minimal payload can suffice. Avoid overcomplicated token refresh or advanced flows for this module.  
2. **Validate on Both Ends**: Client-side checks for user convenience, but always rely on server-side Pydantic validations.  
3. **Thorough E2E**: Cover at least one positive and one negative scenario for both registration and login.  
4. **Document**: Clarify in your README how to spin up the app, run tests, and interpret E2E results.  
5. **Security**: If storing the JWT in localStorage or sessionStorage, be aware of potential XSS or token exposure.

---

## **Submission Deadline**

Please provide by **[Insert Deadline Here]**:

1. **GitHub Repo Link**: Containing your updated front-end code (JWT auth calls + client validations) and E2E tests.  
2. **Module 13 Reflection** (300–500 words).  
3. **README**: Summarize front-end usage, E2E test steps, and Docker Hub link.

Late submissions may be subject to course policy penalties.

---

**Great Work!** By implementing **JWT-based login/registration**, **client-side validation**, and **Playwright** E2E tests, you deliver a secure, tested authentication flow. In **Module 14**, you’ll expand your front-end to handle the full BREAD calculations, completing your final project’s functionality.
