# Module 4: Professional Calculator

## Overview
This project is a professional command-line calculator application developed in Python. It demonstrates object-oriented programming (OOP), comprehensive testing with pytest, and continuous integration using GitHub Actions.

## Features
- Command-line calculator using REPL (Read-Eval-Print Loop)
- Supports basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Input validation and error handling
- Demonstrates both LBYL and EAFP error handling approaches
- Calculation history tracking
- Special commands:
  - `help` – show instructions
  - `history` – display past calculations
  - `exit` – quit the program

## Project Structure
```
module4_calculator/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── app/
│   ├── calculator/
│   │   └── __init__.py
│   ├── calculation/
│   │   └── __init__.py
│   └── operation/
│       └── __init__.py
├── tests/
│   ├── test_calculator.py
│   ├── test_calculations.py
│   └── test_operations.py
├── .gitignore
├── main.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/xing583/module4_calculator.git
cd module4_calculator
```

### Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python main.py
```
## Usage

After running the application, you can enter commands in the REPL:

- add 2 3
- subtract 5 2
- multiply 3 4
- divide 10 2
- history
- help
- exit

## Running Tests
```bash
pytest --cov=app --cov-branch
```

## Test Coverage
This project enforces 100% test coverage using pytest-cov.

## Continuous Integration
GitHub Actions automatically runs tests and enforces 100% coverage on every push.

## Author
Xing Li
