import urllib2


def my_solution():
    number = 2 ** 38
    return str(number)


try:
    solution = my_solution()
    url = 'http://www.pythonchallenge.com/pc/def/' + str(solution) + '.html'
    response = urllib2.urlopen(url)
    if response.code == 200:
        print "next Level! -> " + url
except urllib2.HTTPError:
    print "Wrong Solution!"

#solution: http://www.pythonchallenge.com/pc/def/274877906944.html
