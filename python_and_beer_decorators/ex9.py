from __future__ import print_function

def full_wheat(filling):
    def full_wheat_sandwich():
        print('Apply bottom half of full wheat bun')
        filling()
        print('Apply top half of full wheat bun')
    return full_wheat_sandwich

@full_wheat
def full_wheat_blt():
    print('Apply Bacon')
    print('Apply Lettuce')
    print('Apply Tomatoes')

@full_wheat
def full_wheat_ham_and_cheese():
    print('Apply Ham')
    print('Apply Cheese')



full_wheat_blt()
print()
full_wheat_ham_and_cheese()
