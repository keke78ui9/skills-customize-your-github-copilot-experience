# 📘 Assignment: Testing FastAPI Applications

## 🎯 Objective

Learn to write unit and integration tests for FastAPI APIs using pytest. Students will create tests for endpoints, handle edge cases, and measure code coverage, ensuring their API is robust and reliable.

## 📝 Tasks

### 🛠️ Task 1: Write Unit Tests for Endpoints

#### Description
Write pytest test functions to verify the behavior of each endpoint in the provided FastAPI app. Cover both successful and error scenarios.

#### Requirements
Completed program should:

- Test all main API endpoints (GET, POST, etc.)
- Check for correct status codes and response data
- Include tests for invalid input and error handling


### 🛠️ Task 2: Use Fixtures and Mocking

#### Description
Refactor your tests to use pytest fixtures for setup/teardown and mock any external dependencies (e.g., database calls) to isolate logic.

#### Requirements
Completed program should:

- Use at least one pytest fixture
- Mock external dependencies (e.g., with unittest.mock or pytest-mock)
- Ensure tests do not depend on real external services


### 🛠️ Task 3: Measure and Improve Code Coverage

#### Description
Run your test suite with coverage measurement. Identify any untested code and add tests to achieve at least 90% coverage.

#### Requirements
Completed program should:

- Use pytest-cov to measure code coverage
- Achieve at least 90% coverage
- Add tests for uncovered branches or error cases

---

**Starter code and instructions are provided in this folder.**
