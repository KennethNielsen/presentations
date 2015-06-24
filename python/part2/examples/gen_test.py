from matplotlib import pyplot as plt
import numpy as np

# Polynomial coefficients
coeffs = [2, 4.7, 4.2]

# Make x-values and evaluate the polynomial and add a little noise
x = np.linspace(-10, 10, 1000)
y = np.polyval(coeffs, x) + np.random.random(1000) * 10

# Stack the x, and y values vertically
xy = np.hstack([x.reshape((1000, 1)), y.reshape((1000, 1))])
print xy.shape

# Save to csv file using , as delimiter
np.savetxt("test_data.csv", xy, delimiter=",")

# And plot, just for fun
plt.plot(xy[:,0], xy[:,1])
plt.show()
