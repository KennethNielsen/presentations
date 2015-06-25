import numpy as np
from matplotlib import pyplot as plt
import MySQLdb

connection = MySQLdb.connect(
    'servcinf', 'cinf_reader', 'cinf_reader', 'cinfdata'
)
cursor = connection.cursor()

# Get the three datasets and their metadata
# id 6984
query = 'select x, y from xy_values_stm312 where measurement = 6984 order by id desc'
cursor.execute(query)
data6984tuples = cursor.fetchall()
data6984 = np.array(data6984tuples)

query = 'select id, time, comment from measurements_stm312 where id=6984'
cursor.execute(query)
metadata6984 = cursor.fetchall()[0]

# id 6996
query = 'select x, y from xy_values_stm312 where measurement = 6996 order by id desc'
cursor.execute(query)
data6996tuples = cursor.fetchall()
data6996 = np.array(data6996tuples)

query = 'select id, time, comment from measurements_stm312 where id=6996'
cursor.execute(query)
metadata6996 = cursor.fetchall()[0]

# id 7007
query = 'select x, y from xy_values_stm312 where measurement = 7007 order by id desc'
cursor.execute(query)
data7007tuples = cursor.fetchall()
data7007 = np.array(data7007tuples)

query = 'select id, time, comment from measurements_stm312 where id=7007'
cursor.execute(query)
metadata7007 = cursor.fetchall()[0]


# Cut all the datasets down to only 927 to 948
# 6984
start, end =  np.searchsorted(data6984[:, 0], [927.0, 948.0])
reduced6984 = data6984[start: end, :]

# 6996
start, end =  np.searchsorted(data6996[:, 0], [927.0, 948.0])
reduced6996 = data6996[start: end, :]

# 7007
start, end =  np.searchsorted(data7007[:, 0], [927.0, 948.0])
reduced7007 = data7007[start: end, :]


# Start the plotting
figure = plt.figure()


# Plot the data sets

# 6984, metadata 0 is id and 1 is datetime 2 is comment
datetime = metadata6984[1]
datetimestring = str(datetime.date()) + ' ' + str(datetime.time())
label6984 = str(metadata6984[0]) + ' - ' + datetimestring

axes = figure.add_subplot(311)
axes.set_xlim([927.0, 948.0])
axes.plot(reduced6984[:, 0], reduced6984[:, 1], linewidth=1, label=label6984)
axes.set_title(metadata6984[2])
axes.legend()

# 6996, metadata 0 is id and 1 is datetime 2 is comment
datetime = metadata6996[1]
datetimestring = str(datetime.date()) + ' ' + str(datetime.time())
label6996 = str(metadata6996[0]) + ' - ' + datetimestring

axes = figure.add_subplot(312)
axes.set_xlim([927.0, 948.0])
axes.plot(reduced6996[:, 0], reduced6996[:, 1], linewidth=1, label=label6996)
axes.set_title(metadata6996[2])
axes.legend()

# 7007, metadata 0 is id and 1 is datetime 2 is comment
datetime = metadata7007[1]
datetimestring = str(datetime.date()) + ' ' + str(datetime.time())
label7007 = str(metadata7007[0]) + ' - ' + datetimestring

axes = figure.add_subplot(313)
axes.set_xlim([927.0, 948.0])
axes.plot(reduced7007[:, 0], reduced7007[:, 1], linewidth=1, label=label7007)
axes.set_title(metadata7007[2])
axes.legend()

figure.tight_layout()
plt.show()


# Make combined plot (optional, change True to False to disable)
if True:
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.plot(reduced6984[:, 0], reduced6984[:, 1], 'r-', linewidth=1, label=label6984)
    axes.plot(reduced6996[:, 0], reduced6996[:, 1], 'b-', linewidth=1, label=label6996)
    axes.plot(reduced7007[:, 0], reduced7007[:, 1], 'g-', linewidth=1, label=label7007)
    axes.set_xlim([927.0, 948.0])
    axes.legend()
    plt.show()
