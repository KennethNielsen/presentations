"""A Counter example"""

from pprint import pprint
from collections import Counter

counter = Counter()

for letter in 'Python and beers':
    counter[letter] += 1

pprint(counter)
