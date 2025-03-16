# bank.py
# this program should read in two money amounts and add the two amounts
# Author Mariane McGrath

# Reading each amount (in cent)
amount1= int(input("Enter amount1(in cent):"))
amount2= int(input("Enter amount2(in cent):"))

 # Add the two amounts
total = amount1 + amount2

# Converting the total to euros and cents
euro = total // 100 # Giving the integer number
cents = total % 100 # Calculating cents

#source: Google/ DeepSeek 

# Showing the result in a readable format
print(f"The sum of these is €{euro}.{cents:02d}")