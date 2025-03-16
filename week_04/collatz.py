# asks the user to input any positive integer and outputs
# the successive values of the following calculation.

# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.

#The program end if the current value is one.

while True:
    try:
        x = int(input("Please enter a positive integer: ")) 
      
        if x < 0:
           raise ValueError   
        break  
    except ValueError:

        print("That was not a positive integer. Please try again!")


my_seq =[x]
while  x > 1:
   
    if x % 2 == 0:  
        x = x //2
     
        my_seq.append(x)
        
 
    else:
        x = (x * 3) + 1
         
        my_seq.append(x)

print(*my_seq, sep = ", ")

# Resource: https://www.angela1c.com/projects/problem_set_links/problem4/