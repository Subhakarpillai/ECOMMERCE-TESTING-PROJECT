# E-Commerce Website Testing Project
### Manual Testing | Selenium Automation | Python | Pytest

## 1. Project Overview

A practical Software Quality Assurance project focused on testing the SauceDemo e-commerce web application.

This project covers both Manual Testing and Automation Testing to validate the application's core functionalities, identify potential defects, and verify expected application behavior.

**Application Under Test:** https://www.saucedemo.com/

## 2. Project Objectives

- Understand real-world software testing workflows.
- Design and execute detailed test scenarios and test cases.
- Validate functional requirements of an e-commerce application.
- Automate test cases using Selenium WebDriver and Pytest.
- Maintain test documentation and bug reports.
- Use GitHub for project version control and documentation.

## 3. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and framework |
| VS Code | Development environment |
| Microsoft Excel | Test documentation |
| Git & GitHub | Version control and project hosting |

## 4. Application Modules Tested

**Login Module**
- Valid login credentials
- Invalid username and password
- Invalid username
- Invalid password

**Products Module**
- Verify product listing
- Sort products by price (low to high)
- Sort products by price (high to low)
- Verify product details

**Shopping Cart Module**
- Add a single product
- Add multiple products
- Remove a product
- Verify cart contents

**Checkout Module**
- Checkout with valid customer details
- Validate mandatory fields
- Verify successful order placement

## 5. Manual Testing

Manual testing was performed to validate the application's functional behavior.

Documentation maintained in `Test-Documentation.xlsx`:

- Test Scenarios
- Detailed Test Cases
- Test Execution Results
- Bug Reports

## 6. Automation Testing

Automated the application's major functional test cases using Python, Selenium WebDriver, and Pytest.

**Automation Framework Components**

- `conftest.py` – Shared browser fixture and setup/teardown.
- `pytest.ini` – Pytest configuration.
- `test_login.py` – Login test cases.
- `test_products.py` – Product test cases.
- `test_cart.py` – Shopping cart test cases.
- `test_checkout.py` – Checkout test cases.
- `selenium_basic.py` – Standalone Selenium practice script.

**Automation Approach**

1. Launch Chrome browser using Selenium WebDriver.
2. Navigate to the SauceDemo application.
3. Perform user interactions using Selenium locators.
4. Use explicit waits to handle dynamic page elements.
5. Validate actual results using Python assertions.
6. Execute tests using Pytest.

## 7. Test Execution Results

| Module | Total Test Cases | Passed |
|---|---:|---:|
| Login | 4 | 4 |
| Products | 4 | 4 |
| Shopping Cart | 4 | 4 |
| Checkout | 3 | 3 |
| **Total** | **15** | **15** |

**Execution Status:** 15 Passed, 0 Failed.

## 8. How to Run the Automation Tests

Clone the repository:

```bash

```

Navigate to the automation folder:

```bash
cd Automation-Testing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all test cases:

```bash
pytest -v
```

Run individual test modules:

```bash
pytest tests/test_login.py -v
pytest tests/test_products.py -v
pytest tests/test_cart.py -v
pytest tests/test_checkout.py -v
```

## 9. Skills Demonstrated

- Manual Test Case Design
- Functional Testing
- Test Execution
- Bug Reporting
- Selenium WebDriver
- Python Programming
- Pytest Fixtures
- Explicit Waits
- Assertions
- GitHub Project Management

## 10. Future Enhancements

- Implement Page Object Model (POM).
- Generate automated HTML test reports.
- Integrate test execution with GitHub Actions.
- Expand automation coverage with additional test scenarios.

## 11. Project Outcome

Successfully designed and executed 15 manual and automated test cases covering the major functionalities of an e-commerce application.

This project provided practical experience in test documentation, functional validation, browser automation, and test execution using Pytest.
