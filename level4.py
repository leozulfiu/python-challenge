import urllib2
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
for i in range(300):
    try:
        response = urllib2.urlopen(url)
        text = response.read()
        print text
        nextNumber = re.findall(r'\d+', text)
        if len(nextNumber) == 0:
            print "Ende"
            break
        else:
            nextNumber = nextNumber[0]
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nextNumber
    except urllib2.HTTPError:
        print "Wrong Solution!"

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
for x in range(300):
    try:
        response = urllib2.urlopen(url)
        text = response.read()
        print text
        nextNumber = re.findall(r'\d+', text)
        if len(nextNumber) == 0:
            print "Ende"
            break
        else:
            nextNumber = nextNumber[0]
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nextNumber
    except urllib2.HTTPError:
        print "Wrong Solution!"

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'
for y in range(300):
    try:
        response = urllib2.urlopen(url)
        text = response.read()
        print text
        nextNumber = re.findall(r'\d+', text)
        if len(nextNumber) == 0:
            print "Ende"
            break
        else:
            nextNumber = nextNumber[0]
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nextNumber
    except urllib2.HTTPError:
        print "Wrong Solution!"
