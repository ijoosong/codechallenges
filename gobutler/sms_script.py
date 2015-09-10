#!/usr/local/bin/python
import sys, json, getopt
from collections import OrderedDict

# Store input and output file names
ifile=''
ofile=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

categories = ['title', 'artist', 'author', 'album', 'year']

def to_json():
    with open(ifile) as f, open(ofile, 'w') as f_w:
        output = []
        newli = f.read().split('|-')
        li = [item.strip() for item in newli]
        for item in li:
            buff = item.split('\n')
            if len(buff) > 1:
                output.append( OrderedDict([('title',buff[0]),
                                    ('artist',buff[1]),
                                    ('author',buff[2]),
                                    ('album',buff[3]),
                                    ('year',buff[4])]))
        json.dump(output, f_w, sort_keys = True, indent = 2, ensure_ascii = False)
        f_w.write("\n")


if __name__ == '__main__':
    to_json()
