# Calculating number in Collatz sequence
# Author: Mariane McGrath

# Defining Collatz sequence funtion
def collatz(number):

    # Continue looping until it reaches number 1
    while number != 1:
    
    # If the result is an even number, it divides by 2
        if number % 2 == 0:
            print(number // 2)
            return number // 2
    
    # Otherwise, if it is an off number, it multiplies by 3 and adds 1
        elif number % 2 == 1:
            print(number * 3 + 1)
            return number *3 + 1

# This is the beginning of the program
try:
    n = int (input ("Please enter a positive integer:"))

    # Continues calculations (loops) until it reaches number 1
    while n !=1:

    # Performs Collatz calculations until it reaches 1 
        n = collatz (n)

# Display error message if the user input is not a positive integer
except ValueError:
    print("Please enter a valid integer: ")


# Resources: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff