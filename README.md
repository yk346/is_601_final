# **Module 11: Modeling Calculations and Pydantic Schemas**

## **Module Overview**

In **Module 11**, you will **expand** your application’s database layer by creating a **Calculation** model and **Pydantic** schemas for validating calculation data—**without** adding any endpoints yet. This systematic approach allows you to thoroughly **test** your data design before exposing it via HTTP routes (which will come in **Module 12**). You’ll also explore how a **factory pattern** could help organize different calculation operations (Add, Subtract, Multiply, Divide).  

By the end of this module, you will deepen your practice with:

- Designing and testing a **calculation model** using **SQLAlchemy**.  
- Creating **Pydantic** schemas (e.g., `CalculationCreate`, `CalculationRead`) that govern input/output validation.  
- Incorporating a **factory** design pattern to handle different calculation types elegantly.  
- Maintaining your **CI/CD pipeline**—running unit/integration tests (including a PostgreSQL container) and pushing images to Docker Hub.

**Relevant Course Learning Outcomes (CLOs):**  
- **CLO 3:** Create Python applications with automated testing.  
- **CLO 4:** Set up GitHub Actions for Continuous Integration (CI), automating tests and Docker builds to demonstrate DevOps principles.  
- **CLO 10:** Apply containerization techniques to containerize applications using Docker.  
- **CLO 12:** Integrate Python programs with SQL databases to create and manipulate data.  
- **CLO 13:** Serialize, deserialize, and validate JSON using Python with Pydantic.  
- **CLO 14:** Utilize best practices for software development security by implementing secure authentication and authorization techniques, including encryption, hashing, and encoding.

---

## **Why Focus on the Calculation Model Now (No Routes Yet)?**

1. **Incremental Development:** By finalizing the calculation model and validation logic, you can confidently add routes later, knowing the underlying data structures have been tested.  
2. **Design Patterns (Factory):** This module offers a chance to incorporate a **factory pattern** for handling different calculation types (Add, Subtract, Multiply, Divide), showcasing design-pattern usage within your data layer.  
3. **Solid Testing Foundation:** Verifying the model in isolation ensures your future endpoints (Module 12) can rely on stable, well-tested code.

---

## **Module 11 Outline**

1. **Calculation Model (SQLAlchemy):**  
   - Fields for `a`, `b`, `type` (Add, Sub, Multiply, Divide), optionally `result`.  
   - Potentially reference `user_id` if you’re linking each calculation to a user.  
   - Decide whether you store computed `result` or calculate on the fly.

2. **Pydantic Schemas:**  
   - **CalculationCreate** for incoming data.  
   - **CalculationRead** for returning data (like `id`, `a`, `b`, `type`, `result`).

3. **Factory Pattern for Calculations (Optional):**  
   - A **factory** (e.g., `CalculationFactory`) to instantiate the correct calculation “type” object, centralizing logic for `Add`, `Subtract`, etc.  
   - Encourages a clean, extensible design.

4. **Unit + Integration Testing:**  
   - **Unit Tests:** Validate each calculation type, ensuring correct logic and Pydantic validations.  
   - **Integration Tests:** Spin up a **PostgreSQL** container in GitHub Actions, inserting calculation records and verifying DB operations.

5. **CI/CD Continuation:**  
   - Keep your pipeline from Module 10.  
   - All tests must pass before pushing the updated Docker image to Docker Hub.  

---

## **Hands-On Assignment**

**Title:** Implement and Test a Calculation Model with Optional Factory Pattern  
**Grading Type:** Points  

**Instructions (Be Specific):**

1. **Define the Calculation Model**  
   - Use **SQLAlchemy** (no raw SQL) for fields: `id`, `a`, `b`, `type`, and optionally `result`.  
   - Decide if you store the result or compute on demand. If referencing `user_id`, ensure it’s a valid foreign key.

2. **Create Pydantic Schemas**  
   - **CalculationCreate**: Receives `a`, `b`, and `type` (Add, Sub, Multiply, Divide).  
   - **CalculationRead**: Returns fields like `id`, `a`, `b`, `type`, `result`, etc.  
   - Include relevant validations (e.g., no zero divisor, correct type string/enumeration).

3. **Incorporate a Factory (Optional but Encouraged)**  
   - A **factory** to handle creating or instantiating the correct calculation logic (Add, Sub, Multiply, Divide).  
   - Helps illustrate how design patterns can apply to your data layer.

4. **Write Unit + Integration Tests**  
   - **Unit Tests:**  
     - Validate each operation type (if using the factory, ensure it chooses the correct operation).  
     - Confirm `CalculationCreate` handles invalid input.  
   - **Integration Tests:**  
     - Use your GitHub Actions workflow with a **PostgreSQL** container.  
     - Insert a calculation record, confirm the DB stores correct data.  
     - Test error cases (e.g., invalid type, disallowed operands).

5. **Maintain CI/CD**  
   - Pipeline from Module 10 continues:  
     - Run all tests (user + calculation).  
     - Push to Docker Hub on success.

6. **Submit**  
   - **GitHub Repository Link**: Must have your own code.  
     - **README**: Briefly explain how to run the new tests and link to your Docker Hub repository.  
   - This module focuses solely on modeling and validation; you’ll create actual endpoints (BREAD routes) in **Module 12**.
# **Grading Expectations**

Your submissions for the **Hands-On Assignment** will be evaluated based on the following two criteria:

### **1. Submission Completeness (50 Points)**

- **GitHub Repository Link:**
  - Provided and accessible.
  - Contains all necessary files (`SQLAlchemy` models, Pydantic schemas, application code, tests, GitHub Actions workflow).

- **Screenshots:**
  - **GitHub Actions Workflow:** Screenshot showing a successful run of the GitHub Actions workflow.
  - **Docker Hub Deployment:** Screenshot demonstrating the Docker image has been successfully pushed to Docker Hub.

- **Documentation:**
  - Includes a reflection document addressing key experiences and challenges faced during the development and deployment process.
  - README file contains instructions on how to run tests locally and links to the Docker Hub repository.

### **2. Functionality of Calculation Model and CI/CD Pipeline (50 Points)**

- **Calculation Model:**
  - SQLAlchemy `Calculation` model correctly implemented with fields for `a`, `b`, `type`, and optionally `result`.
  - Proper use of foreign keys if `user_id` is referenced.
  - Implementation of the factory pattern (if attempted) to handle different calculation types.

- **Pydantic Schemas:**
  - **CalculationCreate** schema accurately validates incoming data.
  - **CalculationRead** schema correctly serializes output data, excluding sensitive information.
  
- **Testing and CI/CD:**
  - Comprehensive unit and integration tests are written and pass successfully in the GitHub Actions workflow.
  - CI/CD pipeline is properly configured to build, scan, and deploy the Docker image to Docker Hub without errors.
  - Docker image is functional and can be pulled from Docker Hub, running the application as expected.

---

**Total: 100 Points**
---

## **Reflect**

**Title:** Module 11 Reflection  
**Grading Type:** Points  
**Instructions:**  
Write **600–700 words** covering:

1. **CLO 12 & 13:** How did creating and validating your new calculation model expand your database and Pydantic expertise?  
2. **CLO 3, 4, 10, 14:** Reflect on how unit/integration testing, Docker-based CI, and security considerations played a role—even though no routes exist yet.  
3. **Relating to Earlier Calculator Work:** How do you leverage your prior experience (e.g., a basic Python calculator) to implement polymorphic logic or a factory pattern for the new model?  
4. **Challenges & Solutions:** Note any hurdles (e.g., referencing a user, the factory pattern, test environment setup) and how you overcame them.

---

## **Quiz**

**Title:** Calculation Model & Validation Quiz  
**Grading Type:** Points  

**Instructions:**

1. **Complete the Quiz on Canvas**, focusing on:  
   - SQLAlchemy data modeling for calculations (potential user linkage).  
   - Pydantic validation of various operation types.  
   - Handling logic in unit/integration tests with a DB container.  
   - (Optionally) the factory pattern for distinct calculation objects.

2. **Question Types:**  
   - **Multiple-Choice**: Identify correct approaches to polymorphic or typed calculations.  
   - **Short Answer**: Explain how you’d test or validate a zero-division scenario or an invalid `type` field.

---

## **Tips for Success**

1. **Keep the Future in Mind**: Although no routes yet, design your `Calculation` model so it’s easy to plug into BREAD endpoints next module.  
2. **Validate Thoroughly**: Use Pydantic’s power to reject nonsensical or insecure data early.  
3. **Test at Multiple Levels**: Combine small unit tests (e.g., verifying operation logic) and full integration tests (DB writes/reads).  
4. **Design Patterns**: Embrace the **factory** approach for calculations if you want a more flexible, maintainable design.  
5. **Document**: This is stepping closer to your final project—stay organized and keep a clean README.

---

## **Submission Deadline**

Please provide the following by **[Insert Deadline Here]**:

1. **GitHub Repository Link**: Containing your new calculation model, Pydantic schemas, tests, and CI updates.  
2. **Module 11 Reflection** (600–700 words).  
3. **README** notes: Docker Hub link + instructions for running the new calculation tests locally.

Late submissions may be subject to course policy penalties.

---

**Well Done!** By finalizing the **calculation model** and **schemas** (with robust testing) now, you’ll be fully prepared to implement **BREAD endpoints** for calculations in **Module 12**, ensuring a stable, thoroughly vetted data layer for your evolving **final project**.
