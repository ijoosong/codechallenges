def incr_dict(dct, tup):
    '''given a dct and a tup, iterates through tuple to increment the last element of the tuple in a nested dictionary.  calls each element a node until last leaf'''
    current_dct = dct
    for ele in tup:
        if ele == tup[-1]:
            increment(current_dct, ele)
        elif ele not in current_dct:
            current_dct[ele] = {}
        current_dct = current_dct[ele]
    return dct

def increment(current_dct, ele):
    '''increments the last element. if not available, make equal to 1. else, increment'''
    if ele not in current_dct:
        current_dct[ele] = 1
    else:
        current_dct[ele] += 1

