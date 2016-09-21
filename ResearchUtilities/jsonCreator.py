import json
from random import randint
from math import pow
from researchWords import getWordList

def main():
    (L, A, B) = rgb2lab(218, 55, 67)
    (r, g, b) = lab2rgb(49.55407937199547, 62.70600838856094, 32.35534334585406)
    #makeInverseJSONFiles(4, 125)

def makeInverseJSONFiles(instructNum, trialNum):
    instructShapeIndices = randIndexArr(trialNum)
    trialShapeIndices = randIndexArr(instructNum, instructShapeIndices)

    for i in range(0, 2):
        instructionsHolder = setInstructionsHolder(instructShapeIndices, i)
        trialsHolder = setTrialsHolder(trialShapeIndices, i)
        data = dict()

        data["instructionsHolder"] = instructionsHolder
        data["trialsHolder"] = trialsHolder

        with open('../colorExp/static/json/trial-set-' + i + '.json', 'w') as f:
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

def rgb2lab(r, g, b):
    # Normalize the RGB values
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # D65 standard referent
    X = 0.950470
    Y = 1.0
    Z = 1.088830

    # Second, map sRGB to CIE XYZ
    r = r / 12.92 if r <= 0.04045 else pow((r + 0.055) / 1.055, 2.4)
    g = g / 12.92 if g <= 0.04045 else pow((g + 0.055) / 1.055, 2.4)
    b = b / 12.92 if b <= 0.04045 else pow((b + 0.055) / 1.055, 2.4)

    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / X
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / Y
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / Z

    # Third, map CIE XYZ to CIE L*a*b* and return
    x = pow(x, 1 / 3) if x > 0.008856 else 7.787037 * x + 4.0 / 29
    y = pow(y, 1 / 3) if y > 0.008856 else 7.787037 * y + 4.0 / 29
    z = pow(z, 1 / 3) if z > 0.008856 else 7.787037 * z + 4.0 / 29

    return (116*y - 16, 500*(x-y), 200*(y-z))

def lab2rgb(l, a, b):
    # First, map CIE L*a*b* to CIE XYZ
    y = (l + 16) / 116
    x = y + a / 500
    z = y - b / 200

    # D65 standard referent
    X = 0.950470
    Y = 1.0
    Z = 1.088830

    x = X * x * x * x if x > 0.206893034 else X * (x - 4.0/29) / 7.787037
    y = Y * y * y * y if y > 0.206893034 else Y * (y - 4.0 / 29) / 7.787037
    z = Z * z * z * z if z > 0.206893034 else Z * (z - 4.0 / 29) / 7.787037

    # Second, map CIE XYZ to sRGB
    r = 3.2404542 * x - 1.5371385 * y - 0.4985314 * z
    g = -0.9692660 * x + 1.8760108 * y + 0.0415560 * z
    b = 0.0556434 * x - 0.2040259 * y + 1.0572252 * z

    r = 12.92 * r if r <= 0.00304 else 1.055 * pow(r, 1 / 2.4) - 0.055
    g = 12.92 * g if g <= 0.00304 else 1.055 * pow(g, 1 / 2.4) - 0.055
    b = 12.92 * b if b <= 0.00304 else 1.055 * pow(b, 1 / 2.4) - 0.055

    # Third, discretize and return RGB values
    r = round(255 * r);
    g = round(255 * g);
    b = round(255 * b);

    return (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

main()