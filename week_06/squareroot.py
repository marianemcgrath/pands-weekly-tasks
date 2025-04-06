
# Newton-Raphson Method to calculate a square root of x. Prints an error message if number is negative.

# Formula f(x) = x^2 - N

# Resource: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

number = float(input("Please enter a number: "))

if number < 0:
    print("Error! You entered a negative number, please try again")
else:
    guess = number / 2 
    for _ in range(20): 
        guess = (guess + number/guess) / 2
    
    print(f"The square root of {number} is approximately {guess}")

# Resource: https://www.youtube.com/watch?v=tUFzOLDuvaE Approximating Square Roots w/ Newton's Method
# Resource: https://www.youtube.com/watch?v=nDlip0Mg8tE Python Primer: Implementing Newton's Square Root Approximation
# Resource: https://stackoverflow.com/questions/12219852/square-root-function-in-python-whats-wrong-with-it