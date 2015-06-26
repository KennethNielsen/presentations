import numpy as np
from matplotlib import pyplot as plt
import MySQLdb
import sys

connection = MySQLdb.connect(
    '127.0.0.1', 'cinf_reader', 'cinf_reader', 'cinfdata', port=9997
)
cursor = connection.cursor()


def get_single_data_and_metadata(id_number):
    """Get data and metadata based by id"""
    query = 'select x, y from xy_values_stm312 where measurement = {} order by id desc'
    query = query.format(id_number)
    cursor.execute(query)
    data = np.array(cursor.fetchall())

    fields = ['id', 'time', 'comment']
    fields_string = ','.join(fields)
    query = 'select {} from measurements_stm312 where id={}'
    query = query.format(fields_string, id_number)
    cursor.execute(query)
    metadata = cursor.fetchall()[0]

    metadict = dict(zip(fields, metadata))

    return data, metadict


def get_data_and_metadata(list_of_ids):
    """Returns lists of data and metadata

    Args:
        list_of_ids (list): The ids to get

    Returns:
        list of data sets and list of metadata
    """
    list_of_data = []
    list_of_metadata = []
    for id_number in list_of_ids:
        data, metadata = get_single_data_and_metadata(id_number)
        list_of_data.append(data)
        list_of_metadata.append(metadata)
    return list_of_data, list_of_metadata


def make_subplots_figure(reduced_data_sets, metadatasets, labels):
    """Make figure with datasets as subplots"""
    figure = plt.figure()

    for index in range(len(labels)):
        axes = figure.add_subplot(len(labels), 1, index + 1)
        axes.set_xlim([927.0, 948.0])
        data = reduced_data_sets[index]
        axes.plot(data[:, 0], data[:, 1], linewidth=1, label=labels[index])
        axes.set_title(metadatasets[index]['comment'])
        axes.legend()

    plt.tight_layout()
    plt.show()

def make_combined_figure(reduced_data_sets, labels):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    colors = ['r', 'g', 'b', 'm', 'c', 'y']
    for data, color, label in zip(reduced_data_sets, colors, labels):
        formatstring = color + '-'
        axes.plot(data[:, 0], data[:, 1], formatstring, linewidth=1, label=label)

    axes.set_xlim([927.0, 948.0])
    axes.legend()
    plt.show()


ids = [6984, 6996, 7007]
datasets, metadatasets = get_data_and_metadata(ids)
subplots = True

# Reduce the data sets to go gtom 927 to 948
reduced_data_sets = []
for dataset in datasets:
    start, end =  np.searchsorted(dataset[:, 0], [927.0, 948.0])
    reduced_data = dataset[start: end, :]
    reduced_data_sets.append(reduced_data)

# Produce the labels
labels = []
for meta in metadatasets:
    datetime = meta["time"]
    label = '{} - {} {}'.format(meta["id"], datetime.date(), datetime.time())
    labels.append(label)


if subplots:
    make_subplots_figure(reduced_data_sets, metadatasets, labels)
else:
    make_combined_figure(reduced_data_sets, labels)

