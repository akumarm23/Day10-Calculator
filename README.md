# Simple Calculator Version 0.1

[![License: MIT](https://img.shields.io/badge/License-MIT-pink.svg)](https://opensource.org/licenses/MIT)
[![Version 1.0](https://img.shields.io/badge/Version-1.0-yellowgreen.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-darkblue.svg)](https://www.python.org/downloads/release/python-380/)


## Overview

This is a simple command-line calculator program written in Python. It allows users to perform basic arithmetic operations, such as addition, subtraction, multiplication, and division. The calculator displays a logo at the beginning and prompts the user to enter two numbers and choose an operation. The result is then displayed, and the user has the option to continue calculations with the result or exit the program.

## Features

- Addition, subtraction, multiplication, and division operations
- Dynamic input for numbers and operations
- Continuous calculation with the result
- Graceful exit option

## Requirements

- Python 3.8

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the `main.py` file in your preferred Python environment.

## File Structure

- `main.py`: The main Python script containing the calculator program.
- `logo.py`: A module containing the logo displayed at the beginning of the program.

## Usage

1. Run the `main.py` script.
2. Enter the first number when prompted.
3. Choose an operation from the available symbols (`+`, `-`, `*`, `/`).
4. Enter the second number.
5. The result of the calculation is displayed.
6. Type 'y' to continue calculations with the result or 'n' to exit.

## Sample Execution

```bash
$ python main.py
# [Calculator Logo]
# Enter the first number, n1 = 10
# +   <- Available operations
# - 
# *
# /
# Pick an operation from above: +
# Enter the second number, n2 = 5
# 10 + 5 = 15
# Type 'y' to calculate with 15; else type 'n' to EXIT
```

## Notes

- Division by zero is handled, and the program will display an error message in such cases.
- The calculator continues calculations with the result until the user chooses to exit.

## License

This project is licensed under the [MIT License](LICENSE).

