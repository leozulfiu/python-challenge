import pickle

#peak hell -> pickle

file_Name = 'files/banner.p'
fileObject = open(file_Name, 'r')
serializedObject = pickle.load(fileObject)

for row in serializedObject:
    for column in row:
        for x in xrange(column[1]):
            print(column[0]),
    print "\n",

solution = "channel"
