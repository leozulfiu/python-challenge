import urllib2

text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''


def shift_text(inputText, shifter):
    temp = ""
    index = 0
    while index < len(inputText):
        if inputText[index] == 'y':
            temp += 'a'
        elif inputText[index] == 'z':
            temp += 'b'
        elif inputText[index] == ' ' or inputText[index] == '.' or inputText[index] == ' ' or inputText[index] == '(' \
                or inputText[index] == ')' or inputText[index] == "'":
            temp += inputText[index]
        else:
            temp += chr(ord(inputText[index]) + shifter)
        index += 1
    return temp


try:
    solution = shift_text(text, 2)
    print solution
    currentUrlEnding = 'map'
    solution = shift_text(currentUrlEnding, 2)
    url = 'http://www.pythonchallenge.com/pc/def/' + str(solution) + '.html'
    response = urllib2.urlopen(url)
    if response.code == 200:
        print "next Level! -> " + url
except urllib2.HTTPError:
    print "Wrong Solution!"


