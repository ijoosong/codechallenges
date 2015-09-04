import urllib2

def parse_data():
    url = "https://raw.githubusercontent.com/alexwaters/domainChecker/master/archive/domainDict"
    str = data.read().strip()
    li = [str[i:i+3] for i in xrange(0, len(str),3)]
    for i in range(len(li)):
        li[i] = "http://" + li[i] + ".com"
        print li[i]

if __name__ == '__main__':
    parse_data()
