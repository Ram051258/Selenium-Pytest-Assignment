# Automation Framework Selenium Project

Assignment submission 


## Prerequisites
- Python 3.x
- Selenium WebDriver
- PyTest
- Allure Framework

## Installation

### Clone the repository:

  ```bash
  git clone https://github.com/Ram051258/Selenium-Pytest-Assignment.git
  cd AUTOMATION-FRAMEWORK-SELENIUM

  ```
  ### Install the required dependencies:
  pip install -r requirements.txt

## Running Tests
### To execute the tests and generate an Allure report:

1. Run the test suite
  ```bash
  pytest tests/ --alluredir=reports/allure-results
  ```
2. Generate and view the Allure report
  ```bash
  allure serve reports/allure-results
  ```
This will generate and serve the Allure report locally. Your browser will automatically open with the report view.



