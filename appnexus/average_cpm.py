
#!/usr/local/bin/python
import sys, getopt, csv

# Get data files, delimiter, and groupbys
data_file = ''
delim = ''
group_by = ''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '--data_file':
        data_file = a
    elif o == '--delimiter':
        delimiter = a
    elif o == '--group_by':
        group_by = a
    else:
        print("Usage: %s --data_file=input_file.csv --group_by=advertiser,publisher --delimiter=," % sys.argv[0])

def aggregate():
    reader = loadFile()
    categories, values = getCategoriesValues(reader)


def loadFile():
    """
    Loads file in data_file
    """
    return csv.reader(open(data_file, 'rU'), delimiter=delim)

def getCategoriesValues(reader):
    """
    Separates categories and values and returns as a tuple
    """
    li = [row for row in reader]
    return (li[0], li[1:len(li)])

if __name__ == '__main__':
    aggregate()
