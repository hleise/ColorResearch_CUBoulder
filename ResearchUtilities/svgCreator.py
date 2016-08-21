from random import randint
import math

def main():
    for num in range (0, 4):
        anchorList = []
        numAnchors = randint(5, 10) * 2
        for anchor in range (0, numAnchors):
            randAnchor = getRandAnchor(anchorList)
            anchorList.append(randAnchor)

        orderedList = reorder(anchorList)
        anchorString = ""
        for point in anchorList:
            anchorString += (str(point[0]) +  " " + str(point[1]))
            if point != anchorList[len(anchorList) - 1]:
                anchorString += " "

        printToFile(num, anchorString)

def printToFile(num, anchorString):
    textFile = open(str(num) + ".svg", "w+")
    textFile.write('<?xml version="1.0" encoding="utf-8"?>\n')
    textFile.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
    textFile.write('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">\n')
    textFile.write('<polygon points="' + anchorString + '" style="fill:none;stroke:#000"/>\n')
    textFile.write('</svg>\n')
    textFile.close()

def getRandAnchor(anchorList):
    randAnchor = (randint(5, 95), randint(5, 95))
    if randAnchor in anchorList:
        return getRandAnchor(anchorList)
    return randAnchor

def reorder(anchorList):
    # compute centroid
    cent = (sum([p[0] for p in anchorList]) / len(anchorList), sum([p[1] for p in anchorList]) / len(anchorList))
    # sort by polar angle
    anchorList.sort(key=lambda p: math.atan2(p[1] - cent[1], p[0] - cent[0]))

    return anchorList

main()