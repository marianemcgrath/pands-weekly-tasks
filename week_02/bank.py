# Task 2: Bank 
# This program should read in two money amounts and add the two amounts

# Author Mariane McGrath

# First we read each amount (in cent)
amount1= int(input("Enter amount1(in cent):"))
amount2= int(input("Enter amount2(in cent):"))

# Resource: https://docs.vultr.com/python/examples/add-two-numbers

# Then we add the two amounts
total = amount1 + amount2

# We also need to convert the total to euros and cents
euro = total // 100 # Giving the integer number
cents = total % 100 # Calculating cents

# Resource: DeepSeek (Prompt: "How to calculate euro and cent conversion for 2 integer numbers in a very basic and clean code")

# Showing the result of the function in a readable format in euros and cents
print (f"The sum of these is €{euro}.{cents:02d}")