# QA Automation Toolkit

A personal project for practicing Python and QA automation skills.

## Goals

- Improve Python programming skills
- Learn pytest and Playwright
- Build reusable QA automation utilities
- Prepare for QA Automation interviews

## Project Structure

```text
qa-automation-toolkit/
├── data/
├── tests/
├── utils/
└── README.md
```

## Progress

### Day 1
- Set up Python virtual environment
- Configured GitHub and SSH
- Created project structure
- Implemented data summary utility
- Completed 1 Exercism exercise
- Completed 2 Codewars exercises

### Day 2
## Tech Stack (Learning)
- Python
- Pytest
- Git & Github
- Basic QA Automation Framework

### Day 3
## Topics Covered
- pytest test structure
- pytest.mark.parametrize
- pytest.param with custom test ids
- Positive test cases
- Negative testing with pytest.raises
- Expected failures with pytest.mark.xfail

### Day 5
## Project Structure
qa-automation-toolkit/
│
├── data/
│ └── Test data files
│
├── utils/
│ └── Reusable utility functions
│
├── tests/
│ └── Pytest test cases
│
├── practice/
│ └── Learning exercises
│
└── README.md

## Learning progress
Python:
- Completed Exercism: Black Jack
- Practiced:
  - function reuse
  - boolean logic
  - conditional statements
  - Pythonic coding style

Codewars:
- Keep Hydrated!
- Century From Year

Practiced:
- int()
- //
- %
- if/else logic

### Day 8
## Playwright Practice

Practice website:
https://testautomationpractice.blogspot.com/

Covered elements:

- Textbox
  - Fill input fields
  - Verify input values

- Radio Button
  - Select radio button
  - Verify checked / unchecked state
  - Practice role-based locator and exact matching

- Checkbox
  - Select multiple checkboxes
  - Verify checkbox state

- Dropdown
  - Select options from native `<select>`
  - Verify selected value

- Date Picker
  - Practice locating and interacting with date input fields


### Day 9
## Data-Driven Login Testing
- Added data-driven login testing
- Added login test data in JSON, CSV, and Excel formats
- Used pytest.mark.parametrize
- Added valid and invalid login scenarios
- Used Playwright assertions to verify successful and failed login behavior

### Day 10
## Reporting
- Added HTML test report generation
- Added Allure report integration

### Day 11
## CI/CD Integration

- Integrated Jenkins with GitHub repository
- Configured automated test execution through Jenkins jobs
- Generated Allure test reports after execution
- Supported parameterized test execution

## CI/CD Pipeline

This project uses Jenkins to execute automated tests.

Pipeline stages:
1. Checkout Code
2. Setup Python Environment
3. Install Dependencies
4. Install Playwright Browsers
5. Clean Previous Reports
6. Run Pytest Tests
7. Publish Allure Report

## CI Troubleshooting Notes

- Resolved external website loading timeout issue by adjusting page navigation wait strategy.
- Verified screenshot capture workflow using expected failure tests.


### Day 12
## Added github workflow action files