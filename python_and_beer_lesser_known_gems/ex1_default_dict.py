"""A Default dict example"""

from __future__ import print_function
from collections import defaultdict
import random
from pprint import pprint


def group_with_dicts(items):
    """Group items by rounding to one decimal point"""
    groups = {}
    for item in items:
        key = str(round(item, 1))
        # Annoying first-item-check
        if key in groups:
            groups[key].append(item)
        else:
            groups[key] = [item]
    return groups


def group_with_default_dicts(items):
    """Group items by rounding to one decimal point"""
    groups = defaultdict(list)
    for item in items:
        key = str(round(item, 1))
        groups[key].append(item)
    return groups


def main():
    """Main function"""
    numbers = [random.random() for _ in range(10)]
    print('Numbers:', numbers)
    pprint(group_with_dicts(numbers))
    pprint(group_with_default_dicts(numbers))


main()
