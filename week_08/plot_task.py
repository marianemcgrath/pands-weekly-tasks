# Write a program called plottask.py that displays
# A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

# First, we'll import the necessary distribution, matplotlib.pyplot will help with visualisation
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5,2, 1000)
print(x)                                                                    # We'll get the function to create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2

plt.hist(x, label = "Normal Distribution of x")                             # Then we'll plot it

# Now, we'll create data to plot the function h(x) = x^3
xvalues = np.array (range (0, 10))                                          # First make x values from 0 to 9 (range(0,10) going from 0 to 9) 
yvalues = xvalues**3                                                        # Then,we calculate y values by cubing each x value (with ** we will make xvalues to the power of 3)

plt.plot (xvalues, yvalues, label = "h(x) = $x^3$")                         # plt.plot() will connect points with lines, and we give x velues y values, and a label 'h(x) = x^3'. The $ sign displays the power of 3 neatly.
plt.title("Normal Distribution of x and $x^3$")                             # We'll also add a title to the plot
plt.xlabel("X Values")                                                      # Make sure we have a label for the x-axis
plt.ylabel("Y Values")                                                      # And a label for the y-axis

plt.legend()                                                                # And add a legend to explain which colour or line represents which data
plt.show ()                                                                 # Finally, we'll display the full plot, wwith both the istogram and the line graph.

# Source: https://www.w3schools.com/python/matplotlib_histograms.asp
# Source: https://numpy.org/doc/stable/reference/random/generator.html
# Source: Principles of Data Analytics Class -- Weeks 7 and 8
# Source: https://jupyterbook.org/en/stable/content/math.html (LaTex reference)
