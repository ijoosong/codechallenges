
def incr_dict(dct, tup):
    '''basically you want tup = a, b, c to give {a: {b: {c:1}}}'''

    #base case
    if len(tup) is 1:
        if tup[0] in dct:
            dct[tup[0]] += 1
            return dct
        else:
            dct[tup[0]] = 1
            return dct
    elif len(tup) > 1:
        new_tup = (tup[x] for x in range(1, len(tup)))
        if tup[0] in dct:
            return incr_dict(dct[tup[0]], new_tup)
        else:
            dct[tup[0]] = {}
            return incr_dict(dct[tup[0], new_tup])

'''
    for x in range(len(tup)):
        if tup[x] in buff:
            buff = dct[tup[x]]
        else:
            dct[tup[x]] = {}
            buff = dct[tup[x]]
'''
