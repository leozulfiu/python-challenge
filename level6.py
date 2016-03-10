import zipfile
import re

nextNumber = 90052
archive = zipfile.ZipFile('files/channel.zip', 'r')
textFile = archive.read('90052.txt')


for i in range(len(archive.infolist())):
    print textFile + " Comment: " + archive.getinfo(str(nextNumber)+".txt").comment
    nextNumber = re.findall(r'\d+', textFile)
    if len(nextNumber) == 0:
        print "Ende"
        break
    else:
        nextNumber = nextNumber[0]
        textFile = archive.read(nextNumber + '.txt')

#solution: oxygen
