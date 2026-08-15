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
## GitHub Actions
Added GitHub Actions workflow files
Configured automated pytest execution in GitHub Actions
Verified test execution on a Linux runner
Configured Python environment and project dependencies
Resolved pytest configuration issues in the CI environment

### Day 13
## API Testing
Started API testing with Playwright APIRequest
Practiced sending POST requests
Validated HTTP response status and response body
Created API request bodies using JSON files
Added multiple JSON test data files to the data/ directory
Created a reusable JSON data loading utility
Used Faker to generate dynamic test data
Practiced generating dynamic names, prices, boolean values, and dates
Added a session-scoped request_context fixture
Expanded API testing into CRUD operations
Practiced GET requests for retrieving bookings
Retrieved booking IDs using:
Booking ID
First name and last name
Check-in and check-out dates
Practiced using query parameters for API filtering
Added response status and response body validations
Built an API CRUD test flow using reusable test data and fixtures

## API Testing Example

The project uses the Restful Booker API for API testing practice:

https://restful-booker.herokuapp.com/

Current API testing coverage includes:

Create Booking API
POST request
GET request
JSON request body
Dynamic test data with Faker
Query parameters
Response status validation
Response body validation
Booking data validation
API CRUD testing

## API Test Flow
JSON Test Data
      ↓
Read JSON
      ↓
POST /booking
      ↓
Create Booking
      ↓
Retrieve Booking ID
      ↓
GET /booking/{bookingid}
      ↓
GET /booking?firstname=...&lastname=...
      ↓
GET /booking?checkin=...&checkout=...
      ↓
Validate Responses

### Day 14
## API Response Validation
Headers: Extracted response headers; validated specific values and header presence
Cookies: Extracted cookies from storage_state(); validated specific cookie existence and properties
JSON Schema: Used jsonschema.validate() with a reusable helper to validate response structure, required fields, and data types