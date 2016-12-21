import json
import random
from lab import getOpenTableMatrix
from researchWords import getWordList

# Constant declarations
NUM_SHAPES = 132
NUM_TRIALS = 128
NUM_INSTRUCTIONS = 4

def main():
    (instructShapeIndices, trialShapeIndices) = getIndexLists()
    (practiceSpiky, spiky) = getRandWordList("mixed_spiky")
    (practiceRounded, rounded) = getRandWordList("mixed_rounded")

    openTableJSONFiles(instructShapeIndices, trialShapeIndices, practiceSpiky, practiceRounded, spiky, rounded,  0)
    openTableJSONFiles(instructShapeIndices, trialShapeIndices, practiceSpiky, practiceRounded, spiky, rounded, 1)

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

    assert(len(data["practiceTrials"]) == 4)
    assert (len(data["expTrials"]) == 128)

    with open('../colorExp/static/json/trial-set-' + str(jsonFileId) + '.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

# Returns an array of trials dictionaries
def setTrialHolder(indexList, spikyWords, roundedWords, jsonFileId):
    holder = []
    colorMatrix = getOpenTableMatrix()
    si = 0
    ri = 0

    for i in range(0, len(indexList)):
        trial = dict()

        if jsonFileId % 2 == 0:
            if i in range(0, int(len(indexList) / 4)):
                trial["shape_filename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                si += 1
            elif i in range(int(len(indexList) / 4), int(len(indexList) / 2)):
                trial["shape_filename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                ri += 1
            elif i in range(int(len(indexList) / 2), int((3 * len(indexList)) / 4)):
                trial["shape_filename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                ri += 1
            else:
                trial["shape_filename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                si += 1
        else:
            if i in range(0, int(len(indexList) / 4)):
                trial["shape_filename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                si += 1
            elif i in range(int(len(indexList) / 4), int(len(indexList) / 2)):
                trial["shape_filename"] = "%d-rounded.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                ri += 1
            elif i in range(int(len(indexList) / 2), int((3 * len(indexList)) / 4)):
                trial["shape_filename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = roundedWords[ri][0]
                trial["word2"] = roundedWords[ri][1]
                ri += 1
            else:
                trial["shape_filename"] = "%d-spiky.svg" % indexList[i]
                trial["word1"] = spikyWords[si][0]
                trial["word2"] = spikyWords[si][1]
                si += 1

        if i % 2 == 0:
            trial["rgb1"] = "#da3743"
            trial["rgb2"] = colorMatrix[i]
        else:
            trial["rgb1"] = colorMatrix[i]
            trial["rgb2"] = "#da3743"

        holder.append(trial)

    return holder

main()