# Pands Weekly Tasks
by Mariane McGrath

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![License](https://img.shields.io/badge/License-Educational-purple)

# **Overview**🌇 

Welcome to **Mariane McGrath’s** weekly programming tasks for the **Programming and Scripting** module at **ATU Galway-Mayo**(Year 1/ Semester 1 - 2025).
Each task explores a different core concept of Python programming, from basic syntax to file handling and plotting. 

This repository contains eight weekly tasks, covering:
- Variables, input/output, and string formatting
- Conditionals and loops
- File operations
- Mathematical algorithms
- Data visualisation with plots

## Table of Contents 📑 
- Weekly Tasks
  - [Week 1: Hello World](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_01/helloworld.py)
  - [Week 2: Bank Program](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_02/bank.py)
  - [Week 3: Accounts](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_03/accounts.py)
  - [Week 4: Collatz](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_04/collatz.py)
  - [Week 5: Weekday](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_05/weekday.py)
  - [Week 6: Square Root](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_06/squareroot.py)
  - [Week 7: Letter 'E' Counter](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_07/es.py)
  - [Week 8: Plot Task](https://github.com/marianemcgrath/pands-weekly-tasks/blob/main/week_08/plot_task.py)
- How to Run
- Requirements
- License

# **Tasks** 📚 

## Task 1: Hello World! 
 - This program displays "Hello World!" when it is run

## Task 2: Bank
 This program, called bank.py, prompts the user to enter two amounts in cents, adds the two amounts, and prints the result in the following format: a euro sign and a decimal point between the euro and the cent in the quantity.
Suggested figures for the test: 
  - Enter amount1(in cent): 65
  - Enter amount2(in cent): 180
  - The sum of these is €2.45

**Key Features:**  
- Input handling
- Arithmetic operations
- String formatting
   
## Task 3: Accounts
 - A program called accounts.py that reads a 10-character account number and outputs the account number with only the last four digits showing (and the first six digits replaced with Xs). It also includes a modification to the program to deal with account numbers of any length.

Suggested figures for the test: 
- Please enter a 10-digit account number: 1234567890
- XXXXXX7890

**Key Features:**  
- String slicing and concatenation
- Input protection

## Task 4: Collatz
 - A program called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step, it calculates the next value by taking the current value and, if it is even, dividing it by two. If the current value is odd, it multiplies it by three and adds one. The program ends when it reaches the value one.

Suggested figures for the test:
- Please enter a positive integer: 10
- 10 5 16 8 4 2 1

**Key Features:**  
- While loops
- Even/odd checking

## Task 5: Weekday
This program, called weekday.py, determines whether today is a weekday.
- If it is a weekday, display message: "Yes, unfortunately, today is a weekday."
- If it is the weekend, display a different message: "It is the weekend, yay!"

**Key Features:**  
- Using the `datetime` module
- Conditional statements

** This program requires no user input.

## Task 6: Square Root
 - This program takes a positive floating-point number as input and outputs an approximation of its square root.
 - This program does not use the built-in functions in Python [x ** .5 **or** math.sqrt(x)]
 - To develop the code, the author researched the Newton method for estimating square roots and used the Babylonian method.

Suggested figures for the test:
- Please enter a positive number: 14.5
- The square root of 14.5 is approximately 3.8

**Key Features:**  
- Iterative calculations
- Tolerance checking

## Task 7: "E" count
- The program, called es.py, reads in a text file and outputs the count of the letter 'e' within the text.
* The program should take the filename from an argument on the command line.

Suggested files/ figures for the test:
 - moby-dick.txt
 - 116960

**Key Features:**  
- File handling
- Command-line arguments
- String analysis

## Task 8: Plot Task
 - This program, called plottask.py, displays the following:
 - A histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
 - A plot of the function  h(x)=x3 in the range 0 to 10, in one set of axes
 - A copy of the image of the plot (.png file)

**Key Features:**  
- Data visualisation with `matplotlib`
- Random number generation

## 🚀 How to Use

