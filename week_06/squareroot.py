
# Task 6: Square Root
# Programme that uses the Newton-Raphson Method to calculate a square root of x and prints an error message if number is negative.

# Author: Mariane McGrath


# Newton’s method, also known as Newton-Raphson method is a root-finding algorithm that produces successively better approximations of the roots of a real-valued function.
# Resource: https://www.reddit.com/r/math/comments/2lhxyt/could_someone_explain_to_me_how_newtons_method/ (For a better understanding, in plain terms, how the Newton Raphson method works)


# First, we ask user to enter a number and convert into a floating point number
# The input () function reads the user input as a string, and float() converts it to a float

# We will build a function called square 

def square_root(num):                                   # We will set an error parameter - if between guesses, the number is less than the defined amount
    if num < 0:                                         # If the number is negative (smaller than 0), then an error message is shown
        print ("Error! I cannot calculate the square root of a negative number.")
    elif num == 0:                                      # We'll check if the number is less than zero, if it is we'll issue an error message
        print ("Error! The square root of 0 is 0.")     # Source: Resource: Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press -- Chapter 7
                                                        
                                                        # If the number is positive, we'll keep going

    guess = num / 2                                     # Our first guess is half of the number
    for _ in range (10):                                # And now' we'll make our guess better 10 times
                                                        # Source: https://wiki.python.org/moin/ForLoop

        new_guess = (guess + num / guess) / 2           # Newton's method (formula) makes our guesses more accurate
                                                        # Source: Chat GPT (Prompt: What is the simplest formula, for a beginner, that summarises the Newton-Raphson Method to calculate a square root)
        
        guess = new_guess                               # We'll use the better guess for any following calculations
    return guess                                        # After 10 improvements, we'll update our guess, with the new, more accurate one

# The real program starts here
  
user_input = input ("Enter a positive number: ")        # First, we'll ask the user to type a number
number = float(user_input)                              # Then, we'll convert it to a decimal number (float)     
result = square_root(number)                            # The function will find the approx. square root for the number enter by the user

print (f"The approximate square root of {number} is approx. {result:.1f}") # Finnaly, we'll print an f-string, so we can add variables to text
                                                                           # This part {result:.1f} asks the program to show the result and round the number to one dogit after the decimal point

# Source: https://codedamn.com/news/python/calculate-square-root-in-python
# Source: https://www.youtube.com/watch?v=tUFzOLDuvaE (Approximating Square Roots w/ Newton's Method)
# Source: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/