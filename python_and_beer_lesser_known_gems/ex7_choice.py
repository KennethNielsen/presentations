"""Choice demonstration"""

# Real world story of how I implemented this by hand and it sucked

from __future__ import print_function
from random import random
from math import floor

mylist_of_options = ['Python', 'and', 'beer', 'is', 'fun']

# I want to pick an element at random

# Ok, so I know about random.random, random float from 0.0->1.0

# So multiply with a number to scale it

# Possibly the length of a list

scaled = random() * len(mylist_of_options)

# Think about whether this gives a evenly distributed possibility for each index

# Well, scaled should cover the indices with exactly 1 unit above each index

# So floor it should give a index at random

index_f = floor(scaled)

# oh man, floor returns a float

index = int(index_f)

# So putting it all together

for _ in range(5):
    random_element = mylist_of_options[int(floor(random() * len(mylist_of_options)))]
    print(random_element)

####### OR ....

from random import choice

print('\n\nThe nicer way\n')

for _ in range(5):
    random_element = choice(mylist_of_options)
    print(random_element)
