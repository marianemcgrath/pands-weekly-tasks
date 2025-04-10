# Accounts Task
# Author: Mariane McGrath


# Reading a 10 character account number and displaying the account number with only
# the last 4 digits showing (and the first 6 digits replaced with Xs)

# Enter a 10-digit user account number
account_number = input("Please enter a 10-digit account number: ")

# Ensure the account is 10 characters long
if len(account_number) == 10 and account_number.isdigit():



#Above, the system checks if the input is in the right format that is 10 characters long with len()
# and consists only of digits, using the Boolean (==) denominators

# Resource: Chat GPT promt (Pleasemake me a very basic and clean code that ensures an account number is equal to 10 and an int)



# Mask the digits with 'X', except the last 4
    masked_account = 'XXXXXX' + account_number[-4:]
    
# Output the masked account number
print("Masked account number:", masked_account)

# If the input is invalid, an error message is displayed
print("Invalid input. Please enter a 10-digit numeric account number.")

# Source: https://how.dev/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python