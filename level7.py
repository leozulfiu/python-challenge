from PIL import Image

pngImage = Image.open('files/oxygen.png')
pixelArray = pngImage.load()

string = []
counter = 0
countChars = 0

rgba = pixelArray[counter, 43]
string.append(str(unichr(rgba[0])))
counter = 5

while counter < pngImage.size[0]-22:
    rgba = pixelArray[counter, 43]
    if rgba[0] in range(0, 128):
        string.append(str(unichr(rgba[0])))
        countChars += 1
    counter += 7

print ''.join(string)

solution = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for x in solution:
    print "%c" % (str(unichr(x))),

#solution: http://www.pythonchallenge.com/pc/def/integrity.html
