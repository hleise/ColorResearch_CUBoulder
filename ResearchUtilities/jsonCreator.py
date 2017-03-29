import json
import random
from lab import getOpenTableMatrix, getVariationMatrix
from researchWords import getWordList

# Constant declarations
NUM_SHAPES = 156
NUM_TRIALS = 152
NUM_INSTRUCTIONS = 4

def main():
    (instructShapeIndices, trialShapeIndices) = getIndexLists()
    (practiceSpiky, spiky) = getRandWordList("mixed_spiky")
    (practiceRounded, rounded) = getRandWordList("mixed_rounded")

    openTableJSONFiles(instructShapeIndices, trialShapeIndices, practiceSpiky, practiceRounded, spiky, rounded,  0)

def getRandWordList(wordList):
    list = getWordList(wordList)
    practiceList = []
    trialList = []

    for i in range(0, int(NUM_INSTRUCTIONS / 2)):
        randChoice = random.choice(list)
        practiceList.append(randChoice)
        list.remove(randChoice)
    for i in range(0, int(NUM_TRIALS / 2)):
        randChoice = random.choice(list)
        trialList.append(randChoice)
        list.remove(randChoice)

    random.shuffle(practiceList)
    random.shuffle(trialList)

    return (practiceList, trialList)

# Returns a randomized instructions and trial index list.
def getIndexLists():
    instructShapeIndices = list()
    trialShapeIndices = list(range(0, NUM_SHAPES))

    for i in range(0, NUM_INSTRUCTIONS):
        randChoice = random.choice(trialShapeIndices)
        instructShapeIndices.append(randChoice)
        trialShapeIndices.remove(randChoice)

    random.shuffle(instructShapeIndices)
    random.shuffle(trialShapeIndices)

    return (instructShapeIndices, trialShapeIndices)

def openTableJSONFiles(instructShapeIndices, trialShapeIndices, practiceSpikyWords, practiceRoundedWords, spikyWords, roundedWords, jsonFileId):
    data = dict()
    data["practiceTrials"] = setTrialHolder(instructShapeIndices, practiceSpikyWords, practiceRoundedWords, jsonFileId)
    data["expTrials"] = setTrialHolder(trialShapeIndices, spikyWords, roundedWords, jsonFileId)

    with open('../colorExp/static/json/trial-set-' + str(jsonFileId) + '.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

# Returns an array of trials dictionaries
def setTrialHolder(indexList, spikyWords, roundedWords, jsonFileId):
    holder = []
    colorMatrix = getOpenTableMatrix()
    variationMatrix = getVariationMatrix()
    si = 0
    ri = 0

    for i in range(0, len(indexList)):
        trial = dict()

        if jsonFileId % 2 == 0:
            if i in range(0, int(len(indexList) / 4)):
                trial["shapeFilename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                trial["shapeType"] = "spiky"
                trial["wordType"] = "spiky"
                si += 1
            elif i in range(int(len(indexList) / 4), int(len(indexList) / 2)):
                trial["shapeFilename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                trial["shapeType"] = "spiky"
                trial["wordType"] = "rounded"
                ri += 1
            elif i in range(int(len(indexList) / 2), int((3 * len(indexList)) / 4)):
                trial["shapeFilename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                trial["shapeType"] = "rounded"
                trial["wordType"] = "rounded"
                ri += 1
            else:
                trial["shapeFilename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                trial["shapeType"] = "rounded"
                trial["wordType"] = "spiky"
                si += 1
        else:
            if i in range(0, int(len(indexList) / 4)):
                trial["shapeFilename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                trial["shapeType"] = "rounded"
                trial["wordType"] = "spiky"
                si += 1
            elif i in range(int(len(indexList) / 4), int(len(indexList) / 2)):
                trial["shapeFilename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                trial["shapeType"] = "rounded"
                trial["wordType"] = "rounded"
                ri += 1
            elif i in range(int(len(indexList) / 2), int((3 * len(indexList)) / 4)):
                trial["shapeFilename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                trial["shapeType"] = "spiky"
                trial["wordType"] = "rounded"
                ri += 1
            else:
                trial["shapeFilename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                trial["shapeType"] = "spiky"
                trial["wordType"] = "spiky"
                si += 1

        if i % 2 == 0:
            trial["rgb1"] = "#0090ab"
            trial["rgb2"] = colorMatrix[i]
            trial["hVar"] = variationMatrix[i].get('h')
            trial["cVar"] = variationMatrix[i].get('c')
            trial["lVar"] = variationMatrix[i].get('l')
        else:
            trial["rgb1"] = colorMatrix[i]
            trial["rgb2"] = "#0090ab"
            trial["hVar"] = variationMatrix[i].get('h')
            trial["cVar"] = variationMatrix[i].get('c')
            trial["lVar"] = variationMatrix[i].get('l')

        holder.append(trial)

    return holder

main()