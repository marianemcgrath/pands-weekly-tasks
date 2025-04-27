# A program that reads in a text file and outputs the number of e's it contains
# Author: Mariane McGrath

import sys                                                              # First, we need to be able to read what the user types, so we import sys to access the user entry

try:                                                                    # We'll try to try/ except, assuming the user might make a mistake, so we might have to handle errors
                                                                        # https://www.w3schools.com/python/python_try_except.asp

    moby_dick = sys.argv[1]                                             # We'll take the file that the user entered, and we'll use the second thing (sys.argv[1]) which is the file name
                                                                        # as the first thing (sys.argv[0]) is the name of the program
    with open (moby_dick, "r", encoding = "utf-8") as file:             # Now, we open the text file, we'll read the file, then use .lower() to turn all letters into lowercase          
                                                                        # After, we count how many times 'e' appears in the file    
        count = file.read().lower().count('e')                          # Resource: https://realpython.com/working-with-files-in-python/ (Working With Files in Python)
                                                                        # Resource: DeepSeek AI (Add to my code, a simple function to count both upper and lower cases of the letter 'e')

        print(count)                                                    # Then, we print the final count for the user
                                                                        

except IndexError:                                                           # This error will happen if the user forgot to type the filename after "python es.py" 
    print("Error: Missing filename\nPlease use: python es.py moby_dick.txt") # The program issues a message, on the next line asking user to enter the prompt correctly (program followed by file name)

except FileNotFoundError:                                                    # This error will happen if the filename does not exist
    print(f"Error: File not found")                                          # The program issues a message to let the user know that the file was not found

except:                                                                      # This will catch any other errors, for example, if the file is corrupted
    print("Error: Could not read file")                                      # The program issues a general message
                                                                             # Resource: Matthes, E. (2023) Python Crash Course (3rd edition). San Francisco, US: No Starch Press -- Chapter 11

# Melville Moby Dick - Text File downloaded from https://www.kaggle.com/datasets/gauravduttakiit/melville-moby-dick?resource=download

# Resource: https://docs.python.org/3/library/os.html#files-and-directories 
# Resource: https://www.youtube.com/watch?v=bnVf5IyqEhw