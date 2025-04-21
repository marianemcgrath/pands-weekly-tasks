# A program that reads in a text file and outputs the number of e's it contains
# Author: Mariane McGrath

# Create string 

# Open the file text containing text in read mode
with open("data.txt","r") as f:

# Defining text as a string
    text = f.read()
    e_count = text.count('e')
    print(e_count)



# Resources: https://www.youtube.com/watch?v=kE90BE-jd1U
# Resources: https://realpython.com/working-with-files-in-python/
# Resources: https://www.youtube.com/watch?v=bnVf5IyqEhw
# Sample text downloaded from https://filesamples.com/formats/txt (sample3/ sample1)