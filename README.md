# **Module 14: Completing BREAD for Calculations and Final Project**

## **Module Overview**

In **Module 14**, you will finalize your **BREAD (Browse, Read, Edit, Add, Delete)** functionality for calculations on the front end—integrating it seamlessly with your JWT-secured back end. Additionally, you will implement a **final project feature** that extends beyond basic login and calculations. This feature will require **unit, integration, and end-to-end (E2E) testing** and will be deployed to Docker Hub through your existing CI/CD pipeline. Optionally, you may incorporate **Alembic** for database migrations if your final feature modifies the schema.

By the end of this module, you will submit a **fully functional, secure, tested, and containerized** Python web application as your final deliverable.

### **Relevant Course Learning Outcomes (CLOs)**

- **CLO 3:** Create Python applications with automated testing.
- **CLO 4:** Set up GitHub Actions for Continuous Integration (CI), automating tests and Docker builds to demonstrate DevOps principles.
- **CLO 10:** Apply containerization techniques to containerize applications using Docker.
- **CLO 11:** Create, consume, and test REST APIs using Python.
- **CLO 12:** Integrate Python programs with SQL databases to create and manipulate data.
- **CLO 13:** Serialize, deserialize, and validate JSON using Python with Pydantic.
- **CLO 14:** Utilize best practices for software development security by implementing secure authentication and authorization techniques, including encryption, hashing, and encoding.

---

## **Why Complete BREAD and Add a New Feature Now?**

1. **Comprehensive Scope:** Ensuring full BREAD for calculations completes your core application functions, while the new feature showcases your ability to extend and innovate.
2. **Mastery Demonstration:** Combining final touches on existing features with something entirely new (including all levels of testing) cements your skill set.
3. **Optional Alembic:** Implementing migrations with Alembic (if needed) demonstrates professional DB update handling—useful if your new feature alters the data model.

---

## **Hands-On Assignment: Complete BREAD Functionality for Calculations**

**Title:** Complete BREAD Functionality for Calculations

**Grading Type:** Points

### **Instructions:**

1. **Implement BREAD Endpoints for Calculations:**
   - **Browse (`GET /calculations`):** Retrieve and display all calculations belonging to the logged-in user.
   - **Read (`GET /calculations/{id}`):** Retrieve details of a specific calculation by its ID.
   - **Edit (`PUT /calculations/{id}` or `PATCH /calculations/{id}`):** Update fields of an existing calculation.
   - **Add (`POST /calculations`):** Create a new calculation by specifying the operation and operands.
   - **Delete (`DELETE /calculations/{id}`):** Remove a calculation by its ID.

2. **Integrate Front-End Functionality:**
   - Update the front-end to include forms and interfaces for each BREAD operation.
   - Ensure client-side validations are in place for input fields (e.g., numeric checks, valid operation types).

3. **Extend Playwright E2E Tests:**
   - Write or update Playwright tests to cover:
     - **Positive Scenarios:** Successful creation, retrieval, updating, and deletion of calculations.
     - **Negative Scenarios:** Handling invalid inputs, unauthorized access, and error responses.

---

### **Grading Expectations for Hands-On Assignment**

Your submissions for the **Hands-On Assignment** will be evaluated based on the following two criteria:

#### **1. Submission Completeness (50 Points)**

- **GitHub Repository Link:**
  - Provided and accessible.
  - Contains all necessary files (`BREAD` endpoints, calculation models, tests, GitHub Actions workflow).

- **Screenshots:**
  - **GitHub Actions Workflow:** Screenshot showing a successful run of the GitHub Actions workflow.
  - **Docker Hub Deployment:** Screenshot demonstrating the Docker image has been successfully pushed to Docker Hub.
  - **Application Functionality:** Screenshots of the front-end performing BREAD operations.

- **Documentation:**
  - Includes a reflection document addressing key experiences and challenges faced during the development and deployment process.
  - README file contains instructions on how to run the application, execute tests locally, and links to the Docker Hub repository.

#### **2. Functionality of BREAD Operations (50 Points)**

- **Browse:**
  - All user-specific calculations are retrieved and displayed correctly.

- **Read:**
  - Specific calculations can be accessed with accurate details.

- **Edit:**
  - Calculations can be updated with valid inputs, and changes persist in the database.

- **Add:**
  - New calculations are created successfully with correct operation results.

- **Delete:**
  - Calculations are removed effectively without affecting other data.

---

## **Final Project: Develop an Advanced Feature and Finalize the Application**

**Title:** Develop an Advanced Feature and Finalize the Application

**Grading Type:** Points

### **Instructions:**

1. **Choose and Implement a New Feature:**
   - Select one of the following or propose a similar scope:
     - **User Profile & Password Change:**
       - Add a page or form to let users update profile info (username, email) or change passwords (hash new passwords).
       - Test with unit (change logic), integration (DB updates), E2E (flow from login → profile → password change → re-login).
     - **Additional Calculation Type:**
       - Introduce an advanced operation (exponentiation, modulus, or something custom).
       - Update routes, Pydantic schemas, and the front-end UI.
       - Write tests confirming correct logic (unit), route handling (integration), and front-end usage (E2E).
     - **Report/History Feature:**
       - Provide usage stats or summaries (e.g., total calculations, average operands).
       - Implement routes/data storage, and show a small UI section with these metrics.
       - Thoroughly test logic (unit), route (integration), and UI flow (E2E).

   **(Alternative):** If you have a different idea of comparable complexity (DB changes, new logic, UI integration), clear it with your instructor first.

2. **Develop and Integrate the Feature:**
   - **Backend:**
     - Update SQLAlchemy models if necessary.
     - Create necessary Pydantic schemas for data validation.
     - Implement FastAPI routes to handle the new feature.
   - **Front-End:**
     - Develop new pages or extend existing ones to support the feature.
     - Implement client-side validations as needed.

3. **Testing:**
   - **Unit Tests:** Write tests for new logic or updated functions related to the feature.
   - **Integration Tests:** Ensure new routes interact correctly with the database.
   - **E2E Tests:** Create Playwright tests to validate the entire workflow of the new feature, covering both positive and negative scenarios.

4. **Optional Alembic Migrations:**
   - If the new feature requires changes to the database schema, use Alembic to create and apply migrations.
   - Update the README with instructions on running migrations.

5. **Deployment to Docker Hub:**
   - Ensure your GitHub Actions pipeline:
     - Runs all tests successfully.
     - Builds the Docker image without errors.
     - Pushes the updated Docker image to Docker Hub upon passing all tests.

6. **Submit:**
   - **GitHub Repository Link:**
     - Ensure your repository includes all updated code, tests, and CI configurations.
     - The README should provide:
       - Instructions on running the application.
       - Steps to execute tests locally.
       - Link to your Docker Hub repository.
   - **Final Project Reflection:**
     - Write a reflection (300–500 words) addressing the key points outlined below.

### **Final Project Reflection Instructions**

**Title:** Final Project Reflection

**Grading Type:** Points

**Instructions:**

Write **300–500 words** covering the following points:

1. **Front-End Integration:**
   - How did finishing the BREAD UI and the final feature shape your complete full-stack perspective?

2. **DevOps & Testing:**
   - Discuss how you balanced unit, integration, and E2E tests for your final project.

3. **Security & Best Practices:**
   - Note final approaches to JWT usage, user data protection, and advanced checks for your new feature.

4. **Challenges & Solutions:**
   - Summarize any last hurdles (migrations, advanced feature logic, front-end complexities) and how you addressed them.

---

## **Final Project Grading Rubric**

| **Criteria**                  | **Points** | **Excellent (90-100%)**                                                                 | **Good (70-89%)**                                                              | **Satisfactory (50-69%)**                                                      | **Needs Improvement (<50%)**                                                  |
|-------------------------------|------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Functionality**             | 20         | All BREAD operations and final project feature work flawlessly.                        | Most BREAD operations and final project feature work with minor issues.       | BREAD operations and final feature have noticeable issues affecting usability. | Major functionality issues; BREAD operations or final feature do not work.    |
| **Code Quality & Organization** | 15       | Code is clean, well-organized, and follows best practices. Comprehensive comments.      | Code is mostly clean and organized with some adherence to best practices.      | Code is somewhat organized but lacks consistency and clarity.                  | Code is disorganized, hard to read, and does not follow best practices.      |
| **Security**                  | 15         | Implements robust security measures (JWT, hashed passwords, validation).               | Good security measures with minor lapses.                                     | Basic security measures in place but lacks thorough implementation.            | Weak or missing security measures; vulnerabilities present.                 |
| **Testing**                   | 20         | Comprehensive unit, integration, and E2E tests all pass successfully.                   | Good coverage of tests with most passing; minor gaps in testing.              | Limited test coverage; some tests fail or are missing.                        | Inadequate or no testing; significant tests fail or are missing.             |
| **CI/CD Pipeline**            | 10         | CI/CD pipeline is fully functional, automated, and deploys without errors.              | CI/CD pipeline works with minor issues or delays in deployment.                | CI/CD pipeline is partially functional with notable issues.                   | CI/CD pipeline does not function correctly or is incomplete.                 |
| **Documentation**             | 10         | README is thorough, clear, and includes all required information. Reflection is insightful. | README is clear with most required information. Reflection is adequate.       | README lacks some information; reflection is basic.                           | README is incomplete or unclear; reflection is missing or superficial.      |
| **Front-End Integration**     | 5          | Front-end seamlessly integrates with back-end; user experience is smooth and intuitive. | Front-end mostly integrates well with back-end; minor UX issues.              | Front-end has noticeable integration or UX issues affecting usability.        | Front-end does not integrate effectively with back-end; poor UX.            |
| **Innovation & Extra Features** | 5        | Includes additional features or optimizations beyond requirements.                      | Includes some extra features or improvements.                                 | Meets requirements with minimal additional features.                          | Does not include any extra features beyond basic requirements.               |
| **Final Project Reflection**  | 10         | Reflection is comprehensive, insightful, and addresses all required points thoroughly.   | Reflection addresses most points with adequate depth.                          | Reflection covers some points but lacks depth or completeness.                | Reflection is superficial, incomplete, or missing key points.                |

**Total: 100 Points**

---

## **Tips for Success**

1. **Design First:** Outline your new feature’s data model, routes, and front-end changes before coding.
2. **Code Iteratively:** Complete BREAD, then build the new feature, adding tests at each level (unit → integration → E2E).
3. **Consider Alembic:** If DB schema changes, demonstrate professional migrations.
4. **Document Thoroughly:** This final version is your portfolio piece—be sure it’s well-structured, secure, and tested.

---

## **Submission Requirements**

### **Hands-On Assignment: Complete BREAD Functionality for Calculations**

1. **GitHub Repository Link:**
   - Ensure your repository includes all updated code, tests, and CI configurations related to BREAD operations.
   - The README should provide:
     - Instructions on running the application.
     - Steps to execute tests locally.
     - Link to your Docker Hub repository.

2. **Module 14 Reflection:**
   - Submit your reflection document addressing the key points outlined below.

3. **Quiz:**
   - Complete the quiz on Canvas as specified in the module.

### **Final Project: Develop an Advanced Feature and Finalize the Application**

1. **GitHub Repository Link:**
   - Ensure your repository includes all updated code, tests, and CI configurations related to the final project feature.
   - The README should provide:
     - Instructions on running the application.
     - Steps to execute tests locally.
     - Link to your Docker Hub repository.
     - (If applicable) Instructions on running Alembic migrations.

2. **Module 14 Reflection:**
   - Submit your reflection document addressing the key points outlined above.

3. **Quiz:**
   - Complete the quiz on Canvas as specified in the module.

---

## **Submission Deadline**

All final deliverables (**GitHub repo link**, **Docker Hub link**, **Reflection**) are due by **[Insert Deadline Here]**. Late submissions may be subject to course policy penalties.

---

**Congratulations!** You have built and enhanced a robust full-stack application, culminating in a final project feature that showcases advanced testing, security, and DevOps expertise. This end-to-end solution forms a powerful demonstration of your newly acquired Python web development skills.
