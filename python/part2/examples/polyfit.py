from matplotlib import pyplot as plt
import numpy as np

# Read in data from csv file as one numpy array
xy = np.loadtxt('test_data.csv', delimiter=',')

print "Shape:", xy.shape

# Break the array out into an x and a y array,
# which are the 0'th and 1'st column
x = xy[:, 0]
y = xy[:, 1]

# Try and fit a 3 order polynomial
coefficients = np.polyfit(x, y, 2)
print 'Coefficients:', coefficients

# Calculate y-values for the fit
fitted_y = np.polyval(coefficients, x)

# Plot the value along side each other to evaluate the quality of the fit
plt.plot(x, y, 'b-')
plt.plot(x, fitted_y, 'r-', linewidth=2)
plt.show()
