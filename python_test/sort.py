#!/usr/bin/python
import sys, getopt

# Store input and output file names
ifile=''
ofile=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:], "i:o:")

##########################
# o == option
# a = argument passed to o
##########################
for o, a in myopts:
    if o == '-i':
        ifile = a
    elif o == '-o':
        ofile = a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

def sort_str_and_num():
    """
    sorted list of words and ints
    assuming no special char
    """
    with open(ifile) as f, open(ofile, 'w') as f_w:
        open_file = f.read().strip()
        array = [int(x) if x.isdigit() else x for x in open_file.split(' ')]
        print array
        str_pos = [i for i in range(len(array)) if isinstance(array[i], str)]
        length = len(array)
        array.sort()
        li = []
        sorted_array = []
        y = 0

        while(isinstance(array[-1], str)):
            li.append(array.pop())
            for x in range(length):
                if x in str_pos:
                    sorted_array.append(li.pop())
                else:
                    sorted_array.append(array[y])
                    y += 1

    #        f_w.write(sorted_array)
    print sorted_array
    return sorted_array

if __name__ == '__main__':
    sort_str_and_num()
