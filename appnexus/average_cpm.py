#!/usr/local/bin/python
import argparse, csv

def aggregate():
    """
    Main function that calls other functions to output aggregate
    """
    #parse the command line and get the data file name, categories to group by, and the delimiter
    data_file, group_by, delim = parseCommandLine()

    #open the file and load the values
    reader = loadFile(data_file, delim)
    categories, values = getCategoriesValues(reader)

    #create a custom database of dictionaries
    db = groupCategories(categories, values)

    #find the totals of all of the database groups
    totals = findTotalValues(db, group_by)

    totals, new_categories = findCpm(totals)
    writeOut(totals, new_categories, delim)

    print totals['716_13368']

def writeOut(data_out_totals, data_out_categories, delim):
    with open('_'.join(data_out_categories[0:2]) + '.csv', 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=delim)
        data_writer.writerow(data_out_categories)
        for row in data_out_totals:
            buyer_advertiser = row.split('_')
            data_writer.writerow([buyer_advertiser[0], buyer_advertiser[1], data_out_totals[row]['cpm']])
        

def findCpm(totals):
    """
    Calculates the CPM and returns it as cpm.
    """
    for group_id in totals:
        if totals[group_id]['imps'] > 0:
            totals[group_id]['cpm'] = totals[group_id]['cost']/totals[group_id]['imps']*1000
        else:
            totals[group_id]['cpm'] = totals[group_id]['cost']*1000
    new_categories = ['buyer_member_id', 'advertiser_id', 'average CPM/impression']
    return totals, new_categories

def findTotalValues(db, group_by):
    """
    totals up the imps and cost for each group_by rows
    """
    totals = {}
    for row in db:
        buff = ''
        for item in group_by:
            if buff:
                buff = "_".join([buff, row[item]])
            else:
                buff = row[item]
        if buff in totals:
            totals[buff]['imps'] += float(row['imps'])
            totals[buff]['cost'] += float(row['cost'])
        else:
            totals[buff] = {'imps': float(row['imps']), 'cost': float(row['cost'])}
    return totals

def groupCategories(categories, values):
    """
    Creates a list of dictionaries with categories
    """
    #for each row in values, for each category, return a list with dicts containing key,value
    return [{categories[i]:row[i] for i in range(len(categories))} for row in values]

def parseCommandLine():
    """
    Parses the command line arguments
    """
    parser = argparse.ArgumentParser(description='Script to open --data_file, return cpm by --group_by, delimited by --delimiter')
    parser.add_argument('--data_file', help='What file to open', required=True)
    parser.add_argument('--group_by', help='What fields to group by', required=True)
    parser.add_argument('--delimiter', help='What delimiter separates the fields', required=True)

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
