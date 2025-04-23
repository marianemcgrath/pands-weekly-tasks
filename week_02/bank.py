# Task 2: bank.py
# This program reads in two money amounts and add the two amounts

# Author Mariane McGrath

# Ask the user to enter the first amount in cents.
amount1= int(input("Enter amount1(in cent):"))      # input() shows the message requesting for the user input
                                                    # int() converts the user input into an integer
                                                    # Resource: https://docs.python.org/3/library/functions.html

# Ask the user to enter the second amount in cents.
amount2= int(input("Enter amount2(in cent):"))      

# Define the total for conversion
total = amount1 + amount2                           # Add the two amounts (in cents)
                                                  
# Convert the total to fit the correct format, in euros and cents
euro = total // 100                                 # Gives the integer number
cents = total % 100                                 # Calculates cents

                                                    # 1 euro = 100 cents, so dividing by 100 separates the two different units.
                                                    # Integer division (//), used to discard fractional euros.
                                                    # (%) used to isolate the remainder (cents) after extracting full euros.
                                                    # Resource: DeepSeek (Prompt: "How to calculate euro and cent conversion for 2 integer numbers in a very basic and clean code")
                                                    # Resource: https://docs.python.org/3/tutorial/introduction.html#numbers

print(f"The sum of these is €{euro}.{cents:02d}")   # f-string used to allow different variables to be used and the result of the function in a readable format in euros and cents
                                                    # :02d used to ensure formatting is correct, showing 2 digits for cent.
                                                    # Resource: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals