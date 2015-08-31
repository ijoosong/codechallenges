'''
This will continue to work well as it is O(n * k) where k is the number of keys it has to iterate over.  The tuple being long will not affect this as much as having a lot of keys will.
The tests are found in challenge3_test.py.
'''

def incr_dict(dct, tup):
    '''given a dct and a tup, iterates through tuple to increment the last element of the tuple in a nested dictionary.  calls each element a node until last leaf'''
    current_dct = dct
    for ele in tup:
        if ele == tup[-1]:
            try:
                increment(current_dct, ele)
            except TypeError:
                print ("This key at the end of your tuple already exists as a connecting node.")
        elif ele not in current_dct:
            current_dct[ele] = {}
        try:
            current_dct = current_dct[ele]
        except TypeError:
            print("You cannot grow this key with another key because its been incremented.")
    return dct

def increment(current_dct, ele):
    '''increments the last element. if not available, make equal to 1. else, increment'''
    if ele not in current_dct:
        current_dct[ele] = 1
    else:
        current_dct[ele] += 1
