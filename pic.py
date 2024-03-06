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
        im.close()
        genar = creategenar(piclist)
        newim = genartonew(normalitetwodim(genar,highestfromtwodim(genar)))
        newpath = "C:/Users/Noah/Downloads/numbertests/finals/final" + str(num) + ".png"
        newim = newim.save(newpath)
        print('An image has been succesfully generated for the number ' + str(num) + '!')

def reMakeImages():
    for i in range(9,-1,-1):
        makeImage(i)

def recognize(itempath):
    with Image.open(itempath) as im:
        width, height = im.size
        arr = [[0 for i in range(width)] for j in range(height)]
        for i in range(50):
            for ii in range(50):
                arr[i][ii] = im.getpixel((i,ii))
    numpath = "C:/Users/Noah/Downloads/numbertests/finals/"
    difflist = []
    im.close()
    for i in range(len(os.listdir(numpath))):
        itemnumpath = numpath + os.listdir(numpath)[i]
        with Image.open(itemnumpath) as im:
            numarr = [[0 for m in range(width)] for p in range(height)]
            for j in range(50):
                for jj in range(50):
                    numarr[j][jj] = im.getpixel((j,jj))
            difference = 0
            for j in range(50):
                for jj in range(50):
                    diff = abs(arr[j][jj] - numarr[j][jj][0])
                    #diff = diff * (numarr[j][jj][0] / 255)
                    #if(diff!=0):
                        #print('diff is ' + str(diff) + ' and numarrjjj0 is ' + str(numarr[j][jj][0]))
                    difference = difference + (diff * diff)
            difflist.append(difference)
            #print('The difference between the given image and the number ' + str(i) + ' has been calculated to be ' + str(difference))
    return difflist
            
def lowest(list):
    lowest = list[0]
    for i in range(len(list)):
        if list[i] < lowest:
            lowest = list[i]
    return lowest

def lowestindex(list):
    lowest = list[0]
    lowestindex = 0
    for i in range(len(list)):
        if list[i] < lowest:
            lowest = list[i]
            lowestindex = i
    return lowestindex

userpath = "C:/Users/Noah/Downloads/numbertests/userinput/"
inputs = os.listdir(userpath)
count = 0
avglist = [0,0,0,0,0,0,0,0,0,0]
for item in inputs:
    count = count + 1
    itempath = userpath + item
    curlist = recognize(itempath)
    for i in range(len(curlist)):
        avglist[i] = avglist[i] + curlist[i]
    print('Item number ' + str(count) + ' has been recognized as the number ' + str(lowestindex(recognize(itempath))))
print(avglist)