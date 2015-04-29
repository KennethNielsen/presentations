"""namedtuple example"""

from __future__ import print_function
from collections import namedtuple

def arange(start, end, step):
    """Arange dummy function"""
    print('arange', start, end, step)


def get_data_from_db(data_id):
    """Get data from db dummy function"""
    print('get_data_from_db', data_id)


def plot(x, y, title):
    """plot dummy function"""
    print('plot with title: "{}"'.format(title))


################################### Without named tuple
def without_named_tuple():
    """Without named tuple"""
    print('Without named tuple')

    # A dataset is: data_id, comment, step, start, end
    datasets = (
        (1234, 'this is the one', 0.1, 45, 55),
        (1345, 'no wait this is', 0.2, 40, 60),
        (1456, 'I know I got it now', 0.2, 40, 60),
        (1567, 'OK maybe not .. let\'s try something else', 0.05, 40, 60),
        (1678, 'here we go again', 0.05, 40, 62),
    )

    for dataset in datasets:
        print('\n### Process dataset', dataset)
        # Remember a dataset is: data_id, comment, step, start, end
        x = arange(dataset[3], dataset[4], dataset[2])
        y = get_data_from_db(data_id=dataset[0])
        plot(x, y, title=dataset[1])


####################################### With named tuple
def with_named_tuple():
    """With named tuple"""
    print('\n\nWith named tuple')

    dataset = namedtuple('dataset', 'data_id comment step start end')
    #dataset = namedtuple('dataset', ['data_id', 'comment', 'step', 'start', 'end'])

    datasets = (
        dataset(1234, 'this is the one', 0.1, 45, 55),
        dataset(1345, 'no wait this is', 0.2, 40, 60),
        dataset(1456, 'I know I got it now', 0.2, 40, 60),
        dataset(1567, 'OK maybe not .. let\'s try something else', 0.05, 40, 60),
        dataset(1678, 'here we go again', 0.05, 40, 62),
    )

    for dataset in datasets:
        print('\n### Process', dataset)
        x = arange(dataset.start, dataset.end, dataset.step)
        y = get_data_from_db(data_id=dataset.data_id)
        plot(x, y, title=dataset.comment)


if __name__ == '__main__':
    #without_named_tuple()
    with_named_tuple()
