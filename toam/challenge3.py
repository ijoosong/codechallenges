def incr_dict(dct, tup):
    current_dct = dct
    for ele in tup:
        if ele == tup[-1]:
            increment(current_dct, ele)
        elif ele not in current_dct:
            current_dct[ele] = {}
        current_dct = current_dct[ele]
    return dct

def increment(current_dct, ele):
    if ele not in current_dct:
        current_dct[ele] = 1
    else:
        current_dct[ele] += 1

