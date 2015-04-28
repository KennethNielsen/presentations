"""namedtuple example"""

from collections import namedtuple

def arange(start, end, step):
    print('arange', start, end, step)

def get_data_from_db(id):
    print('get_data_from_db', id)

def plot(x, y, title):
    print('plot with title: "{}"'.format(title))


# Without named tuple

print('Without named tuple')

# A dataset is: id, comment, step, start, end
datasets = (
    (1234, 'this is the one', 0.1, 45, 55),
    (1345, 'no wait this is', 0.2, 40, 60),
    (1456, 'I know I got it now', 0.2, 40, 60),
    (1567, 'OK maybe not .. let\'s try something else', 0.05, 40, 60),
    (1678, 'here we go again', 0.05, 40, 62),
)

for dataset in datasets:
    # Remember a dataset is: id, comment, step, start, end
    x = arange(dataset[3], dataset[4], dataset[2])
    y = get_data_from_db(id=dataset[0])
    plot(x, y, title=dataset[1])


# With named tuple

print('\n\nWith named tuple')

dataset = namedtuple('dataset', 'id comment step start end')
#dataset = namedtuple('dataset', ['id', 'comment', 'step', 'start', 'end'])

datasets = (
    dataset(1234, 'this is the one', 0.1, 45, 55),
    dataset(1345, 'no wait this is', 0.2, 40, 60),
    dataset(1456, 'I know I got it now', 0.2, 40, 60),
    dataset(1567, 'OK maybe not .. let\'s try something else', 0.05, 40, 60),
    dataset(1678, 'here we go again', 0.05, 40, 62),
)

for dataset in datasets:
    x = arange(dataset.start, dataset.end, dataset.step)
    y = get_data_from_db(id=dataset.id)
    plot(x, y, title=dataset.comment)
