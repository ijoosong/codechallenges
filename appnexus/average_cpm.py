#!/usr/local/bin/python
import argparse, csv

def aggregate():
    """
    Main function that calls other functions to output aggregate
    """
    (data_file, group_by, delim) = parseCommandLine()
    reader = loadFile(data_file, delim)
    categories, values = getCategoriesValues(reader)
    
    print categories
    print values[0]
    print group_by
#    for value in values:
        

def parseCommandLine():
    """
    Parses the command line arguments
    """
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--data_file', help='Description for what file to open', required=True)
    parser.add_argument('--group_by', help='Description for what fields to group by', required=True)
    parser.add_argument('--delimiter', help='Description for what delimiter separates the fields', required=True)

    args = vars(parser.parse_args())
    return (args['data_file'], args['group_by'].split(','), args['delimiter'])

def loadFile(data_file, delim):
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
