import json
from lab import rgb2lab, lab2rgb
from random import randint
from researchWords import getWordList

def main():
    makeInverseJSONFiles(4, 125)

def makeInverseJSONFiles(instructNum, trialNum):
    instructShapeIndices = randIndexArr(instructNum)
    trialShapeIndices = randIndexArr(trialNum, instructShapeIndices)

    for i in range(0, 2):
        instructionsHolder = setInstructionsHolder(instructShapeIndices, i)
        trialsHolder = setTrialsHolder(trialShapeIndices, i)
        data = dict()

        data["instructionsHolder"] = instructionsHolder
        data["trialsHolder"] = trialsHolder

        with open('../colorExp/static/json/trial-set-' + str(i) + '.json', 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

# Returns an array of unique random indices that aren't in the passed restrictedIndices array.
def randIndexArr(numIndices, restrictedIndices = []):
    indices = []
    while len(indices) < numIndices:
        index = randint(0, 130)
        if ((index not in indices) and (index not in restrictedIndices)):
            indices.append(index)
    return indices

# Returns an array of instruction case dictionaries
def setInstructionsHolder(indexList, isEven):
    holder = []

    for i in indexList:
        trial = dict()
        trial["word1"] = "word %d.1" % i
        trial["word2"] = "word %d.2" % i
        trial["rgb1"] = "#da3743"
        trial["rgb2"] = "#da3743"
        if i % 2 == isEven:
            trial["shape_filename"] = "%d-spiky.svg" % i
        else:
            trial["shape_filename"] = "%d-rounded.svg" % i

        holder.append(trial)

    return holder

# Returns an array of trial dictionaries
def setTrialsHolder(indexList, isEven):
    holder = []

    for i in indexList:
        for j in range(0, 2):
            trial = dict()
            trial["word1"] = "word %d.1" %(i)
            trial["word2"] = "word %d.2" %(i)
            trial["rgb1"] = "#da3743"
            trial["rgb2"] = "#da3743"
            if j % 2 == isEven:
                trial["shape_filename"] = "%d-spiky.svg" % i
            else:
                trial["shape_filename"] = "%d-rounded.svg" % i

            holder.append(trial)

    return holder

main()