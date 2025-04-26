# A program that reads in a text file and outputs the number of e's it contains
# Author: Mariane McGrath

from pathlib import Path
path = moby_dick.txt


import sys
# Resource: https://stackoverflow.com/questions/61031785/syntax-error-using-sys-argv-as-argument-in-function (sys.arg function )
try:
    path = sys.argv [1]
    with open (moby_dick.txt,"rt", encoding='utf-8') as file:                                # Open the file text containing text in read mode
                                                                        # Text file downloaded from https://www.kaggle.com/datasets/gauravduttakiit/melville-moby-dick?resource=download
                                                                        # Resource: https://www.w3schools.com/python/python_file_handling.asp
        text = file.read()
        e_count = text.lower().count('e')
        print (f"The number of total 'e' letters on the file is"+ {e_count})

except IndexError:
    print("Error: Please provide a filename (e.g., python counter.py moby_dick.txt)")
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' not found. Please check:")
    print("- The file exists in the same directory as your script")
    print("- You spelled the filename correctly")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Resources: https://www.youtube.com/watch?v=kE90BE-jd1U
# Resources: https://realpython.com/working-with-files-in-python/
# Resources: https://www.youtube.com/watch?v=bnVf5IyqEhw
# Sample text downloaded from https://filesamples.com/formats/txt (sample3/ sample1)