
def sort_str_and_num(array):
    """sorted list of words and ints"""
    """assuming no special char"""
    str_pos = [i for i in range(len(array)) if isinstance(array[i], str)]
    print str_pos
    return sorted(array)

print sort_str_and_num(['hello', 1, 4, 'bye', 3, 5, 'what'])
