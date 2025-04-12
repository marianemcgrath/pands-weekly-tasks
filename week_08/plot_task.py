# Write a program called plottask.py that displays
# A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5,2, 1000)
print(x)
# Plotting a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
x = np.random.normal(5, 2, 1000)
plt.hist(x, label = "x")

# Plotting of the function h(x)=x3 in the range 0 to 10, on the one set of axes
xvalues = np.array (range (0, 10))
yvalues = xvalues**3

plt.plot (xvalues, yvalues, label = "x^3")
plt.title(" Histogram and plot of x and x^3")
plt.legend()
plt.show ()

# Resource: https://www.w3schools.com/python/matplotlib_histograms.asp
# Resource: https://numpy.org/doc/stable/reference/random/generator.html