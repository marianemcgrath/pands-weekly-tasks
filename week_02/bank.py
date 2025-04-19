# Task 2: bank.py
# This program reads in two money amounts and add the two amounts

# Author Mariane McGrath

# Ask the user to enter the first amount in cents.
# input() shows the message requesting for the user input
# int() converts the user input into an integer
amount1= int(input("Enter amount1(in cent):"))

# Resource: https://docs.python.org/3/library/functions.html

# Ask the user to enter the second amount in cents.
amount2= int(input("Enter amount2(in cent):")) 

# Define the total for later conversion
total = amount1 + amount2                           # Add the two amounts (in cents)

# Convert the total to euros and cents
euro = total // 100                                 # Gives the integer number
cents = total % 100                                 # Calculates cents

# 1 euro = 100 cents, so dividing by 100 separates the two different units.
# Integer division (//), used to discard fractional euros.
# (%) used to isolate the remainder (cents) after extracting full euros.
                                                    
# Resource: DeepSeek (Prompt: "How to calculate euro and cent conversion for 2 integer numbers in a very basic and clean code")
# Resource: https://docs.python.org/3/tutorial/introduction.html#numbers

# Shows the result of the function in a readable format in euros and cents
# f-string used to allow different variables directly
# :02d used to ensure formatting is correct, showing 2 digits for cent.
print(f"The sum of these is €{euro}.{cents:02d}")

# Resource: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals