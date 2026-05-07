# 📌 UI + API Hybrid Automation Framework – ExpandTesting Notes App

## 📖 Project Overview

This project is a hybrid automation framework built using **Python, Selenium, Pytest, and Requests**. It covers both **UI automation and API automation** for the ExpandTesting Notes Application.

The framework follows a modular structure with Page Object Model (POM), reusable fixtures, logging, and reporting support.

---

## 🔗 Application Under Test

- UI: https://practice.expandtesting.com/notes/app  
- API: https://practice.expandtesting.com/notes/api/api-docs/

---

# 🧪 SECTION 1 – UI AUTOMATION

## 🎯 Objectives

- Automate login and notes functionalities
- Implement Page Object Model (POM)
- Capture screenshots on failure
- Add logging support
- Maintain clean test structure

---

## ⚙️ Tech Stack

- Python  
- Selenium WebDriver  
- Pytest  
- Logging  

---

## 📁 Project Structure


PYTEST_CAPSTONE_PROJECT/
│
├── tests/
│ ├── ui/
│ │ ├── test_login.py
│ │ ├── test_notes.py
│
├── pages/
│ ├── login_page.py
│ ├── notes_page.py
│
├── reports/
├── logs/
├── screenshots/
├── conftest.py


---

## 🚀 Features

- Page Object Model (POM)
- Reusable Selenium fixtures
- Screenshot capture on failure
- Logging for test execution
- Clean separation of test logic and page logic

---

## ▶️ Run UI Tests

```bash
pytest tests/ui -v
📸 Outputs
Logs: reports/test.log
Screenshots: reports/screenshots/
🧪 SECTION 2 – API AUTOMATION
🎯 Objectives
Automate REST API testing for Notes App
Validate authentication and CRUD operations
Combine API testing with Pytest
⚙️ Tech Stack
Python
Requests
Pytest
📁 API Test Structure
tests/
├── api/
│   ├── test_login_api.py
│   ├── test_notes_api.py
🔑 API Scenarios Covered
User Login API
Create Note API
Get Notes API
Update Note API
Delete Note API
🚀 API Flow
Login and get authentication token
Create a note using token
Validate note creation
Fetch notes
Delete note
Verify deletion
▶️ Run API Tests
pytest tests/api -v
🔄 HYBRID TESTING (UI + API)

This framework ensures:

API creates and validates data
UI verifies the same data visually
End-to-end system validation
🧰 COMMON FEATURES (conftest.py)
WebDriver setup and teardown
Logging configuration
Screenshot capture on failure
Reusable fixtures
📊 REPORTING
Logs → reports/test.log
Screenshots → reports/screenshots/
Pytest console output
🧠 KEY CONCEPTS USED
Page Object Model (POM)
API Testing with Requests
Pytest Fixtures
Hooks (pytest_runtest_makereport)
Modular Automation Framework
Hybrid Testing Strategy
▶️ RUN FULL SUITE
pytest -v

For parallel execution:

pytest -n auto