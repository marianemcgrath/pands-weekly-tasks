# Task 4: Collatz
# Calculating number in Collatz sequence

# Author: Mariane McGrath


# Define Collatz sequence funtion in which 'number' is starting integer
def collatz(number):           
    print (number)                          # Shows the first number in the sequence

    if number == 1:                         # If the number is equal to 1
        return number                       # Then the sequence ends (as per Collatz "hypothesis", in which all starting numbers eventually reach 1)
        
    if number % 2 == 0:                     # If the number is even
        return collatz (number//2)          # Divide it by 2

    else:                                   # If the number is odd
        return collatz ((number * 3) + 1)   # Multiply number by 3 and add 1

# Resource: https://www.youtube.com/watch?v=1imEkPu-jGQ (A Recursive approach to the Collatz Sequence in Python - Solving "Automate the Boring Stuff" project using a recursive function)
                                               
while True:                                 # Infinite loop that inly exits if the valid input is entered
    try:
        number = int(input("Enter integer number:"))     # Ask the user for an integer number
        if number <=0:                                   # If a negative integer is entered
            print ("Please enter a POSITIVE INTEGER.")   # Error message is issued
        else:                                            # If user input is a positive integer (as required)
            collatz (number)                             # Then the program shows the sequence
            break                                        # And loop ends
    except ValueError:                                   # If any other value such as a string or a floating-point number is entered
        print (" Something went wrong, please enter a valid integer") # An error message is displayed to user and loop continues.

# Resource: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

# Resource: https://docs.python.org/3/reference/compound_stmts.html (The try statement)