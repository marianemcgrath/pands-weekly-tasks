# Task 05: Weekday
# A program that outputs whether or not today is a weekday

# Author: Mariane McGrath


# First we import datetime information to learn what date and time it is
import datetime

# The formula below is used to identify date, time as well as days of the week
week_day = datetime.datetime. today().weekday()

# Considering 0 to 4 is Monday until Friday, 
# 5 and 6 are Sat and Sun
if week_day < 5:                                                # If true, it means today is a weekda
    print ("Yes, unfortunately today is a weekday.")            # The function displays a message that represents the minus craic factor that symbolises a weekday
else:                                                           # The 'else' block runs if the 'if' condition is false (i.e., Sat/Sun, 5-6)
    print ("It is the weekend, yay!")                           # The function displays a happy message because it's the weekend


# Resource 1: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Resource 2: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python
# Resource 3: https://www.w3schools.com/python/python_conditions.asp