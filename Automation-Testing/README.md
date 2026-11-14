# SauceDemo Automation Testing Project

## Project Overview
This project focuses on automating the SauceDemo e-commerce web application using Selenium WebDriver with Python and Pytest.

The framework follows the Page Object Model (POM) design pattern to improve code reusability, maintainability, and readability.

## Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Visual Studio Code
- Git & GitHub

## Project Structure

```text
Automation-Testing/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Automated Test Modules

| Module | Test Cases |
|---|---:|
| Login | 4 |
| Products | 4 |
| Cart | 4 |
| Checkout | 3 |
| **Total** | **15** |

## Framework Design

The project uses the Page Object Model (POM).

- Page classes contain web element locators and reusable methods.
- Test files contain test scenarios and assertions.
- `conftest.py` manages the WebDriver fixture.
- `pytest.ini` contains Pytest configuration.
- HTML reports provide test execution results.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Test Execution

Run all automated test cases:

```bash
pytest -v
```

Generate an HTML execution report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## Test Execution Results

- Total Test Cases: 15
- Passed: 15
- Failed: 0
- Skipped: 0

## Future Enhancements

- Implement data-driven testing.
- Add screenshots for failed test cases.
- Integrate automation tests with Jenkins.
- Implement cross-browser testing.

## Author

Subhakar M

Software Testing | Selenium Automation | Python | Pytest
