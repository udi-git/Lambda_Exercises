# AWS Lambda & Python Practices

A repository containing 13 hands-on AWS Lambda functions written in Python.

This project focuses on core Serverless concepts, including JSON event payload parsing, dynamic routing, environment variable configuration.
---

## Project Structure

The repository is organized into 13 dedicated directories (`exercise1` through `exercise13`). Each folder contains:
- The Python function source code (`.py`).
- Screenshots validating successful execution for various test events.

---

## Exercises Overview

| Exercise | Description | Source File | Test Execution Screenshots |
| :--- | :--- | :--- | :--- |
| **01. Hello World** | Basic Lambda function returning a simple string response. | [`lambda-hello-world.py`](./exercise1/lambda-hello-world.py) | [View](./exercise1/exercise1.png) |
| **02. Event Handling** | Dynamic service routing based on `s3`, `db`, or default input keys. | [`S3-Db-Event.py`](./exercise2/S3-Db-Event.py) | [View](./exercise2/exercise2.png) |
| **03. Environment Variables** | Fetching runtime configuration using `os.environ`. | [`envoirment-variables.py`](./exercise3/envoirment-variables.py) | [Standard](./exercise3/exercise3.png) / [Custom Key](./exercise3/exercise3-1.png) |
| **04. Basic Math** | Performing arithmetic operations on numeric values inside the JSON event. | [`Lambda-Math-Calculation.py`](./exercise4/Lambda-Math-Calculation.py) | [View](./exercise4/exercise4.png) |
| **05. String Formatting** | Dynamic response formatting using f-strings. | [`Lambda-String-Manipulation.py`](./exercise5/Lambda-String-Manipulation.py) | [View](./exercise5/exercise5.png) |
| **06. Greeting Message** | Extracting a name parameter with fallback defaults and custom payloads. | [`Greeting-Message.py`](./exercise6/Greeting-Message.py) | [Default](./exercise6/exercise6.png) / [Custom Payload](./exercise6/exercise6-1.png) |
| **07. Even or Odd** | Evaluating integers using modulo (`% 2`) logic. | [`Even-Or-Odd.py`](./exercise7/Even-Or-Odd.py) | [Even Test](./exercise7/excercise7.png) / [Odd Test](./exercise7/excercise7-1.png) |
| **08. Uppercase String** | Converting input text to uppercase using `.upper()`. | [`UpperCase_String.py`](./exercise8/UpperCase_String.py) | [Test 1](./exercise8/exercise8.png) / [Test 2](./exercise8/exercise8-1.png) |
| **09. Word Length** | Calculating string length with Python's built-in `len()`. | [`Word_Length.py`](./exercise9/Word_Length.py) | [Test 1](./exercise9/exercise9.png) / [Test 2](./exercise9/exercise9-1.png) |
| **10. String Concatenation** | Extracting and joining multiple JSON string values into a unified response. | [`Concatenate_Strings.py`](./exercise10/Concatenate_Strings.py) | [Test 1](./exercise10/exericse10.png) / [Test 2](./exercise10/exericse10-1.png) |
| **11. Square a Number** | Calculating the square exponent of an input integer. | [`Square_a_Number.py`](./exercise11/Square_a_Number.py) | [Test 1](./exercise11/exercise11.png) / [Test 2](./exercise11/exercise11-1.png) |
| **12. Subtraction** | Executing subtraction between two dynamic numerical parameters. | [`Simple_Subtraction.py`](./exercise12/Simple_Subtraction.py) | [Positive Result](./exercise12/exercise12.png) / [Negative Result](./exercise12/exercise12-1.png) |
| **13. Minimum Number** | Comparing two payload numbers and returning the minimum value. | [`Minimum_of_Two_Numbers.py`](./exercise13/Minimum_of_Two_Numbers.py) | [Min 1](./exercise13/exercise13.png) / [Min 2](./exercise13/exercise13-1.png) |

---

## How to Deploy & Test

1. Copy the function logic from any `.py` file into the **AWS Lambda Console** (`lambda_function.py`).
2. Set up a **Test Event** with the corresponding JSON payload as shown in the exercise screenshots.
3. Click **Deploy** and then **Test** to view execution results and CloudWatch output logs.
