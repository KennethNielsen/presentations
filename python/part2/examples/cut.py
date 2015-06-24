from matplotlib import pyplot as plt
import numpy as np

# Read in data from csv file as one numpy array
xy = np.loadtxt('test_data.csv', delimiter=',')

print "Shape:", xy.shape

# Break the array out into an x and a y array,
# which are the 0'th and 1'st column
x = xy[:, 0]
y = xy[:, 1]

# We want to cut out the part of the data where the x-values are between
# -2.3 and 7.8. X-values are sorted, so we can use searchsorted, never use on
# unsorted data
left_index, right_index = np.searchsorted(x, [-2.3, 7.8])
print "Boundaries:", left_index, right_index
reduced_x = x[left_index: right_index]
reduced_y = y[left_index: right_index]
print "Min and max of reduced x", reduced_x.min(), reduced_x.max()

# Plot the cut out values along side the entire data set, to check the result
figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(x, y, 'b-', linewidth=2)
axes.plot(reduced_x, reduced_y, 'r-', linewidth=0.8)
plt.show()
