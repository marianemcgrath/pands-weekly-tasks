# Task 3: Accounts

# In this task, the program reads a 10 character account number and displays the account number with only
# the last 4 digits showing (and the first 6 digits replaced with Xs)

# Author: Mariane McGrath

# We will make sure this is an infinite loop, and will keep asking for user input until it is valid

while True:                                                             
    acc_number = input ("Please enter your 10 digit account number:")   # First we ask the user to enter an account number

    if len(acc_number) != 10:                                           # The first check uses (!=) to ensure the user input has exactly 10 characters
        print("Invalid input. Please enter exactly 10 digits")     
        continue

    if not acc_number.isdigit():                                        # The second check, using the isdigit () function, ensures ONLY digits are entered by user
            print("Invalid input. Please enter only digits (0-9)")
            continue
            
    break                                                               # If both checks are passed, the loop will stop     
     
                                                                        # Source: https://realpython.com/python-while-loop/ (Python while Loops: Repeating Tasks Conditionally)
                                                                        # Source: Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press (Chapter 7)
# After receiving avalid input, we'll calculate how many digits to mask

total_digits = len (acc_number)                                         # We'll get the account number
mask = total_digits - 4                                                 # Now, we mask all numbers from input, except the last 4
showstr = acc_number [mask:]                                            # This part shows where the slice is placed, which is before the last 4 digits to be shown
                                                                        # (in this case after the hidden or masked number)
                                                                        # Source: Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press (Chapter 4)print("X" * mask + showstr)                                             # Output the masked account number
                                                                        # Source: https://www.youtube.com/watch?v=H2uYYigqCnE (Python Code Challenge - Credit Card Mask)

# Extra comments: Above, the system checks if the input is in the right format required of exactly 10 characters long with len() and 
# using the boolean (==) denominators. To include an input of any length, and taking into account that usually account numbers are normally longer than 6 digits,
# #the first loop check can change to  "if len(acc_number) >= 6:" and this would ensure the account is equal to or larger than 6 digits, all numbers. If for strings to be added
# the isdigit() function can also be removed.   

# Source: https://how.dev/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
