# Weekly Task 05
# A program that outputs whether or not today is a weekday

# Author: Mariane McGrath


# First we import datetime information to learn what date and time it is

import datetime

# The formula below is used to identify date, time as well as days of the week
week_day = datetime.datetime. today().weekday()

# Considering 0 to 4 is Monday until Friday, 
# 5 and 6 are Sat and Sun

if week_day < 5: 
    print ("Yes, unfortunately today is a weekday.")

else:  
    print ("It is the weekend, yay!")


# Resource 1: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Resource 2: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python