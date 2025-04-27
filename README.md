# Pands Weekly Tasks
by Mariane McGrath

# **Overview**  🌇 

Welcome to **Mariane McGrath’s** weekly programming tasks for the **Programming and Scripting** module at **ATU Galway-Mayo**(Year 1/ Semester 1 - 2025).
Each task explores a different core concept of Python programming, from basic syntax to file handling and plotting. 

This repository contains eight weekly tasks, covering:
- Variables, input/output, and string formatting
- Conditionals and loops
- File operations
- Mathematical algorithms
- Data visualisation with plots

## 📑 Table of Contents
- [Overview](#overview)
- [Weekly Tasks](#weekly-tasks)
  - [Week 1: Hello World](#week-1-hello-world)
  - [Week 2: Bank Program](#week-2-bank-program)
  - [Week 3: Accounts](#week-3-accounts)
  - [Week 4: Collatz](#week-4-collatz)
  - [Week 5: Weekday](#week-5-weekday)
  - [Week 6: Square Root](#week-6-square-root)
  - [Week 7: Letter 'E' Counter](#week-7-letter-e-counter)
  - [Week 8: Plot Task](#week-8-plot-task)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [License](#license)

# **Tasks** 📚 

## Task 1: Hello World! 
 - This program displays "Hello World!" when it is run

## Task 2: Bank
 This program, called bank.py, prompts the user to enter two money amounts (in cents), adds the two amounts, and prints the result in the following format: a euro sign and a decimal point between the euro and the cent in the quantity.
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

# **Resources** 📝

Various resources were consulted to aid learning and ensure best practices. Key references include:
Online:
- Python Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
- W3Schools Python Tutorials: [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
- Stack Overflow Discussions for troubleshooting specific issues: [https://stackoverflow.com/](https://stackoverflow.com/)
- Matplotlib Documentation for plotting tasks: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- Real Python Tutorials (for deeper Python insights): [https://realpython.com/](https://realpython.com/)
- GeeksforGeeks Python Tutorials (especially for file handling and loops): [https://www.geeksforgeeks.org/python-programming-language/](https://www.geeksforgeeks.org/python-programming-language/)
  
Book:
- Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press

AI Sources:
- Both Chat GPT and DeepSeek were utilised in parts of this project, including the creation of this ReadMe file.
  The specific prompts were referenced throughout each task.

# **License** 📜
This project is for educational purposes as part of the Programming and Scripting course at ATU.
Feel free to reference or adapt, but please avoid plagiarism.
