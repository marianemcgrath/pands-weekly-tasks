
# Task 6: Square Root
# Programme that uses the Newton-Raphson Method to calculate a square root of x and prints an error message if number is negative.

# Author: Mariane McGrath

# Newton’s method, also known as Newton-Raphson method is a root-finding algorithm that produces successively better approximations of the roots of a real-valued function.
# Formula f(x) = x^2 - a

# Resource: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

# Now, we get to the code:

# Ask user to enter a number and convert into a floating point number
# The input () function reads the user input as a string, and float() converts it to a float

number = float(input("Please enter a number: "))


if number < 0:                                                          # We use an error message if number entered is a negative number
    print("Error! You entered a negative number, please try again")
else:                                                                  
    guess = number / 2                                                      # If it is a positive number, the formula divides it by 2, to guess the square root
    # We'll ask for 20 iterations of the method (using the formula), to improve our square root estimate
    # The more iterations, the more accurate the approximation will be
    # We use _ as the loop variable because we don't actually need its value
    for _ in range(20): 
        guess = (guess + number/guess) / 2
    
    print(f"The square root of {number} is approximately {guess}")      # Function added, as it looks good when trying to include strings and numbes, 
                                                                        # that outputs the number the user entered and its square root

# Resource: https://www.youtube.com/watch?v=tUFzOLDuvaE Approximating Square Roots w/ Newton's Method
# Resource: https://www.youtube.com/watch?v=nDlip0Mg8tE Python Primer: Implementing Newton's Square Root Approximation
# Resource: https://stackoverflow.com/questions/12219852/square-root-function-in-python-whats-wrong-with-it