
# Task 6: Square Root
# Programme that uses the Newton-Raphson Method to calculate a square root of x and prints an error message if number is negative.

# Author: Mariane McGrath


# Newton’s method, also known as Newton-Raphson method is a root-finding algorithm that produces successively better approximations of the roots of a real-valued function.

# Resource: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo (Calculating the square root using Newton Raphson method)
# Resource: https://www.reddit.com/r/math/comments/2lhxyt/could_someone_explain_to_me_how_newtons_method/ (For a better understanding, in plain terms, how the Newton Raphson method works)


# Ask user to enter a number and convert into a floating point number
# The input () function reads the user input as a string, and float() converts it to a float

# We will build a function called square 

def square_root(num):                                   # We'll set an error parameter - if between guesses, the number is less than the defined amount
    if num < 0:                                         # If the number is negative (smaller than 0)
        print ("Error! I cannot calculate the square root of a negative number.") # An error message is shown
    elif num == 0:
        print ("Error! The square root of 0 is 0.")
   
    guess = num / 2                                     # Our first guess is half of the number
    for _ in range (10):                                # We'll make the guess better 10 times
        new_guess = (guess + num / guess) / 2          # This formula makes our guesses more accurate
        guess = new_guess                              # We'll use the better guess for any following calculations
        
    return guess                                       # After 10 improvements, we'll have the final guess

# This program starts here
  
user_input = input ("Enter a positive number: ")       # First we'll ask the user to type a number
number = float(user_input)                             # Then we'll convert it to a decimal number (float)      
result = square_root(number)

print (f"The approximate square root of {number} is approx. {result:.1f}")


# Resource: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm (Python Square function using newton's algorithm)
# Resource: https://www.youtube.com/watch?v=tUFzOLDuvaE (Approximating Square Roots w/ Newton's Method)
# Resource: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/