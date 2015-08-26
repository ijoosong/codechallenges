def idct(dct, tup):
    current_dct = dct
    for ele in tup:
        print ele
        if ele == tup[-1]:
            if ele not in current_dct:
                current_dct[ele] = 1
            else:
                current_dct[ele] += 1
        elif ele not in current_dct:
            current_dct[ele] = {}
            print 'inside if statement'
            print current_dct
        current_dct = current_dct[ele]
        print 'outside if statement'
        print current_dct
        print dct
    return dct
