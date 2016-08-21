import json
from random import randint

def main():
    instructIndices = randIndexArr(4)
    trialIndices = randIndexArr(30, instructIndices)

    instructionsHolder = setInstructionsHolder(instructIndices)
    trialsHolder = setTrialsHolder(trialIndices)
    data = dict()

    data["instructionsHolder"] = instructionsHolder
    data["trialsHolder"] = trialsHolder

    with open('../colorExp/static/json/trial-set-1.json', 'w') as f:
        json.dump(data, f)

# Returns an array of unique random indices that aren't in the passed restrictedIndices array.
def randIndexArr(numIndices, restrictedIndices = []):
    indices = []
    while len(indices) < numIndices:
        index = randint(0, 99)
        if ((index not in indices) and (index not in restrictedIndices)):
            indices.append(index)
    return indices

# Returns an array of instruction case dictionaries
def setInstructionsHolder(indexList):
    holder = []

    for i in indexList:
        trial = dict()
        trial["word1"] = "word %d.1" % i
        trial["word2"] = "word %d.2" % i
        trial["rgb1"] = "#4285F4"
        trial["rgb2"] = "#0F9D58"
        if i % 2 == 0:
            trial["shape_filename"] = "%d-spiky.svg" % i
        else:
            trial["shape_filename"] = "%d-rounded.svg" % i

        holder.append(trial)

    return holder

# Returns an array of trial dictionaries
def setTrialsHolder(indexList):
    holder = []

    for i in indexList:
        for j in range(0, 2):
            trial = dict()
            trial["word1"] = "word %d.1" %(i)
            trial["word2"] = "word %d.2" %(i)
            trial["rgb1"] = "#4285F4"
            trial["rgb2"] = "#0F9D58"
            if j % 2 == 0:
                trial["shape_filename"] = "%d-spiky.svg" % i
            else:
                trial["shape_filename"] = "%d-rounded.svg" % i

            holder.append(trial)

    return holder

main()