#Write a program called plottask.py that displays:

#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range 0 to 10, 
#on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc).

#Please put a copy of the image of the plot (.png file) into the repository

import numpy as np

x = np.random.normal(5,2, 1000)

print(x)

import matplotlib.pyplot as plt

import numpy as np


x = np.random.normal(5,2, 1000)

plt.hist((x**3))
plt.show() 

plt.xlabel ('x')
plt.ylabel ('x^3')
plt.title ('Plot Task')




# Resource: https://www.w3schools.com/python/matplotlib_histograms.asp