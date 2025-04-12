#Write a program called plottask.py that displays:
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range 0 to 10, 
#on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc).

#Please put a copy of the image of the plot (.png file) into the repository

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5,2, 1000)
print(x)
# Plotting a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
x = np.random.normal(5, 2, 1000)
plt.hist(x, label = "x")

# Plotting of the function h(x)=x3 in the range 0 to 10, on the one set of axes
xvalues = np.array (range (0, 10))
yvalues = xvalues*3

plt.plot (xvalues, yvalues, label="x*3")
plt.title("X*3")
plt.legend()
plt.show ()

# Resource: https://www.w3schools.com/python/matplotlib_histograms.asp
# Resource: https://numpy.org/doc/stable/reference/random/generator.html