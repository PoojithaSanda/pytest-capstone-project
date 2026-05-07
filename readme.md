# Hybrid UI + API Automation Framework

## Overview

This project is a hybrid test automation framework built for the Expand Testing Notes application using Python. The framework combines Selenium UI automation and REST API automation in a single project to validate both frontend and backend functionality.

The goal of this project is to demonstrate a real-world automation framework structure using:

* Selenium WebDriver for UI testing
* Pytest as the test runner
* Requests library for API testing
* Page Object Model (POM)
* Logging, screenshots, and reporting
* End-to-end hybrid validation

The framework is designed to be clean, scalable, reusable, and easy to maintain.

---

# Application Under Test

### UI Application

[https://practice.expandtesting.com/notes/app](https://practice.expandtesting.com/notes/app)

### API Documentation

[https://practice.expandtesting.com/notes/api/api-docs/](https://practice.expandtesting.com/notes/api/api-docs/)

---

# Technologies Used

| Technology         | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming language     |
| Selenium WebDriver | UI automation            |
| Pytest             | Test execution framework |
| Requests           | API testing              |
| Pytest-xdist       | Parallel execution       |
| Allure Reports     | Reporting                |
| Logging            | Execution tracking       |
| Docker             | Container support        |
| Jenkins            | CI/CD integration        |

---

# Project Structure

```text
PYTEST_CAPSTONE_PROJECT/
│
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_notes.py
│   │
│   ├── api_tests/
│   │   └── test_notes_api.py
│   │
│   ├── e2e/
│   │   ├── test_api_to_ui.py
│   │   └── test_ui_to_api.py
│
├── pages/
│   ├── login_page.py
│   └── notes_page.py
│
├── utils/
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── docker-compose.yml
└── Jenkinsfile
```

---

# Framework Design

## Page Object Model (POM)

The framework follows the Page Object Model design pattern.

Each page in the application has a separate Python class that contains:

* Web element locators
* Reusable methods
* Page-specific actions

This helps keep the test scripts clean and improves maintainability.

---

# Test Coverage

## UI Automation Scenarios

The UI automation covers:

* User login
* Notes creation
* Notes validation
* UI element interaction
* Browser actions
* Negative login validation

### UI Features

* Explicit waits
* Reusable page methods
* Screenshot capture on failures
* Logging support
* Modular test structure

---

## API Automation Scenarios

The API automation validates:

* User authentication
* Token generation
* Create note API
* Get notes API
* Update note API
* Delete note API
* Response status validation
* JSON response validation

### API Features

* Reusable request methods
* Token handling
* Dynamic data usage
* Assertions for response validation

---

# Hybrid End-to-End Testing

One of the important parts of this project is hybrid testing.

The framework validates data between API and UI layers.

## Example Flows

### API → UI

1. Create a note using API
2. Login through UI
3. Verify the same note is displayed in the application

### UI → API

1. Create a note from UI
2. Fetch notes using API
3. Validate the created note from backend response

This approach helps verify complete system integration.

---

# Fixtures and Hooks

The project uses Pytest fixtures for reusable setup and teardown.

## Common Fixtures

* Browser setup
* Browser teardown
* API authentication token
* Shared test data

## Hooks Used

### pytest_runtest_makereport

Used for:

* Capturing screenshots on failure
* Logging failed test information

---

# Logging and Reporting

## Logs

Execution logs are stored inside:

```text
reports/test.log
```

## Screenshots

Failed test screenshots are stored inside:

```text
reports/screenshots/
```

## Allure Reports

The framework supports Allure reporting.

Generate the report using:

```bash
allure serve allure-results
```

---

# Installation

## Step 1: Clone the Repository

```bash
git clone <repository-url>
```

## Step 2: Navigate to Project Folder

```bash
cd PYTEST_CAPSTONE_PROJECT
```

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run Complete Test Suite

```bash
pytest -v
```

---

## Run UI Tests Only

```bash
pytest tests/ui -v
```

---

## Run API Tests Only

```bash
pytest tests/api_tests -v
```

---

## Run End-to-End Tests

```bash
pytest tests/e2e -v
```

---

## Run Tests in Parallel

```bash
pytest -n auto
```

---

# Docker Support

The project includes Docker configuration for containerized execution.

Run the framework using:

```bash
docker-compose up --build
```

---

# Jenkins Integration

A Jenkinsfile is included for CI/CD pipeline execution.

The pipeline can be configured to:

* Install dependencies
* Execute tests
* Generate reports
* Publish results

---

# Best Practices Followed

* Modular framework design
* Reusable code structure
* Separation of test and page logic
* Explicit waits instead of hard waits
* Centralized configuration
* Scalable test architecture
* Reusable fixtures and utilities
* Hybrid validation strategy

---

# Challenges Solved During Development

During development, the following automation challenges were handled:

* Dynamic waits and synchronization issues
* Token handling for APIs
* Data sharing between UI and API layers
* Screenshot handling for failures
* Test execution stability
* Parallel execution support

---

# Future Improvements

Possible future enhancements:

* Database validation
* Excel or JSON driven test data
* Cloud execution using Selenium Grid
* GitHub Actions integration
* Advanced reporting dashboards
* Cross-browser execution

---

# Author

Developed as a Selenium + Pytest + API Hybrid Automation Capstone Project.

This project demonstrates practical automation framework implementation skills including UI testing, API testing, framework design, reporting, and CI/CD integration.
