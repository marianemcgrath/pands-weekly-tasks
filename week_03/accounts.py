# Task 3: Accounts
# In this task, the program reads a 10 character account number and displays the account number with only
# the last 4 digits showing (and the first 6 digits replaced with Xs)

# Author: Mariane McGrath

# Enter a user account number
acc_number = input ("Please enter your 10 digit account number: ")

# Ensuring the account has 10 digits and it is an integer, a loop was added, to ensure the user has
# the correct number of digits. If not, an error message is issued.

if len(acc_number) == 10 and acc_number.isdigit():
    valid_input = True                              # This exits the loop once user has the correct input
else:
    print("Invalid input. Please enter 10 digits.")

# Resource: DeepSeek AI - Promt (Please make me a very basic and clean code that ensures an account number has 10 an int)

# Check how many numbers/ characters the account number has (length of the input)
string_length = len (acc_number)

# Mask all numbers from input, except the last 4
mask = string_length - 4

# This part shows where the slice is placed, which is before the last 4 digits to be shown
showstr = acc_number [mask:]
    
# Output the masked account number
print("X" * mask + showstr)

# Above, the system checks if the input is in the right format that is exactly 10 characters long with len() and using the boolean (==)
# denominators and isdigit() for a numeric digits only entry, if the loop is removed (from line 13 to line 16), non-numerical
# characters can also be a part of the account number, as well as an input of any length.

# Source: https://www.youtube.com/watch?v=H2uYYigqCnE (Python Code Challenge - Credit Card Mask)
# Source: https://how.dev/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python