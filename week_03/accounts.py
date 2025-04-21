# Task 3: Accounts
# In this task, the program reads a 10 character account number and displays the account number with only
# the last 4 digits showing (and the first 6 digits replaced with Xs)

# Author: Mariane McGrath

# Enter a user account number
while True:                                    
    acc_number = input ("Please enter your 10 digit account number:")  

    if len(acc_number) == 10:                  # Boolean added to check the user imput has 10-digits
         if acc_number.isdigit():              # isdigit () function added to ensure ONLY numbers are entered by user
            break                              # Stops the loop, once user enters 10 digits
    else:                                      # If entered number does not meet requirements, issue error message.
          print("Invalid input. Please enter 10 digits")
else:
        print("Invalid input. Please enter exactly 10 digits")

# Ensuring the account has 10 digits and it is an integer, a loop was added, to ensure the user has
# the correct number of digits. If not, an error message is issued.

# Source: https://realpython.com/python-while-loop/ (Python while Loops: Repeating Tasks Conditionally)
# Source: Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press (Chapters 7)

# Check how many numbers/ characters the account number has (length of the input)
str_length = len (acc_number)

# Mask all numbers from input, except the last 4
mask = str_length - 4

# This part shows where the slice is placed, which is before the last 4 digits to be shown (in this case after the hidden or masked number)
showstr = acc_number [mask:]
    
# Output the masked account number
print("X" * mask + showstr)

# Source: https://www.youtube.com/watch?v=H2uYYigqCnE (Python Code Challenge - Credit Card Mask)

# Above, the system checks if the input is in the right format required of exactly 10 characters long with len() and 
# using the boolean (==) denominators. To include an input of any length, the loop should be removed (Lines 8, 11 - 17)
# Additionally, as account numbers are normally longer than 6 digits, the first loop check can change to  "if len(acc_number) >= 6:"
# and this would ensure the account is equal to or larger than 6 digits, all numbers.   

# Sources: https://how.dev/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
