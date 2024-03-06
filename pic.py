import os
from PIL import Image

def creategenar(list):
    genar = [[0 for i in range(len(list[0]))] for j in range(len(list[0][0]))]
    for i in range(len(list)):
        for ii in range(len(list[0])):
            for iii in range(len(list[0][0])):
                genar[ii][iii] = genar[ii][iii] + list[i][ii][iii]
    return genar

def genartonew(genar):
    newim = Image.new('RGB',(50,50),(255,255,255))
    for i in range(len(genar)):
        for ii in range(len(genar[0])):
            newim.putpixel( (i,ii), (int(genar[i][ii]),int(genar[i][ii]),int(genar[i][ii])))
    return newim

def highestfromtwodim(list):
    highest = 0
    for i in range(len(list)):
        for ii in range(len(list[0])):
            if list[i][ii]>highest:
                highest = list[i][ii]
    return highest

def normalitetwodim(list, highest):
    goal = 255 / highest
    for i in range(len(list)):
        for ii in range(len(list[0])):
            list[i][ii] = list[i][ii] * goal
    return list

def makeImage(num):
    path = "C:/Users/Noah/Downloads/numbertests/templates/template" + str(num) + ".png"
    with Image.open(path) as im:
        piclist = []
        #im.show()
        for m in range(10):
            for s in range(10):
                arr = [[0 for i in range(50)] for j in range(50)]
                for i in range(50):
                    for ii in range(50):
                        arr[i][ii] = im.getpixel((i+s*51,ii+m*51))
                        #print(arr[ii][i])
                    #print('something big has happened')
                piclist.append(arr)
        genar = creategenar(piclist)
        newim = genartonew(normalitetwodim(genar,highestfromtwodim(genar)))
        newpath = "C:/Users/Noah/Downloads/numbertests/finals/final" + str(num) + ".png"
        newim = newim.save(newpath)
        print('An image has been succesfully generated for the number ' + str(num) + '!')

for i in range(9,5,-1):
    makeImage(i)