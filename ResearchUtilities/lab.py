from math import atan, sin, cos, sqrt, pow, pi

# Converts a given rgb value to its corresponding lab value
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

# Converts a given lab value to its corresponding rgb value
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
    r = round(255 * r)
    g = round(255 * g)
    b = round(255 * b)

    return (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

# Converts a given lab value to its corresponding hcl value
def lab2hcl(l, a, b):
    h = atan(b / a)
    c = sqrt( pow(a, 2) + pow(b, 2) )
    return (h, c, l)

# Converts a given hcl value to its corresponding lab value
def hcl2lab(h, c, l):
    a = c * cos(h)
    b = c * sin(h)
    return (l, a, b)

# Returns a list of variations of the open table red in rgb hex format
def getOpenTableMatrix():
    colorMatrix = []
    OTL, OTA, OTB = rgb2lab(0, 144, 171)
    openTableRed = lab2hcl(OTL, OTA, OTB)
    C10 = 0.1 * sqrt(32768)
    C5 = 0.05 * sqrt(32768)

    for x in range(0, 3):
        for c in [-C10, -C5, 0, C5, C10]:
            for l in [-10, -5, 0, 5, 10]:
                # Makes the color matrix of hex values starting from hcl(-5%, -5%, -5%)
                tempLabL, tempLabA, tempLabB = hcl2lab(openTableRed[0], openTableRed[1] + c, openTableRed[2] + l)
                labL, labA, labB = tempLabL, -tempLabA, -tempLabB
                red, green, blue = lab2rgb(labL, labA, labB)
                colorMatrix.append(toHex(red, green, blue))
        for h in [-pi / 5, -pi / 10, 0, pi / 10, pi / 5]:  # -10%, -5%, 0%, 5%, 10%
            for l in [-10, -5, 0, 5, 10]:
                # Makes the color matrix of hex values starting from hcl(-10%, -10%, -10%)
                tempLabL, tempLabA, tempLabB = hcl2lab(openTableRed[0] + h, openTableRed[1], openTableRed[2] + l)
                labL, labA, labB = tempLabL, -tempLabA, -tempLabB
                red, green, blue = lab2rgb(labL, labA, labB)
                colorMatrix.append(toHex(red, green, blue))

    # Inserts the 2 extra instances of openTableRed so len(colorMatrix) is divisible by 4
    colorMatrix.insert(50, "#0090ab")
    colorMatrix.insert(151, "#0090ab")

    return colorMatrix

def getOpenTableDict():
    colorMatrix = []
    OTL, OTA, OTB = rgb2lab(0, 144, 171)
    openTableRed = lab2hcl(OTL, OTA, OTB)
    C10 = 0.1 * sqrt(32768)
    C5 = 0.05 * sqrt(32768)

    for c in [-C10, -C5, 0, C5, C10]:
        for l in [-10, -5, 0, 5, 10]:
            tempLabL, tempLabA, tempLabB = hcl2lab(openTableRed[0], openTableRed[1] + c, openTableRed[2] + l)
            labL, labA, labB = tempLabL, -tempLabA, -tempLabB
            red, green, blue = lab2rgb(labL, labA, labB)
            colorMatrix.append({'L': openTableRed[2] + l, 'a': labA, 'b': labB, 'c': openTableRed[1] + c,
                                'h': openTableRed[0], 'r': red, 'g': green, 'b2': blue})
    for h in [-pi / 5, -pi / 10, 0, pi / 10, pi / 5]:  # -10%, -5%, 0%, 5%, 10%
        for l in [-10, -5, 0, 5, 10]:
            tempLabL, tempLabA, tempLabB = hcl2lab(openTableRed[0] + h, openTableRed[1], openTableRed[2] + l)
            labL, labA, labB = tempLabL, -tempLabA, -tempLabB
            red, green, blue = lab2rgb(labL, labA, labB)
            colorMatrix.append({'L': openTableRed[2] + l, 'a': labA, 'b': labB, 'c': openTableRed[1],
                                'h': openTableRed[0] + h, 'r': red, 'g': green, 'b2': blue})

    return colorMatrix

def getVariationMatrix():
    variationMatrix = []
    for x in range(0, 3):
        for c in [-10, -5, 0, 5, 10]:
            for l in [-10, -5, 0, 5, 10]:
                variationMatrix.append({'h': 0, 'c': c, 'l': l})
        for h in [-10, -5, 0, 5, 10]:
            for l in [-10, -5, 0, 5, 10]:
                variationMatrix.append({'h': h, 'c': 0, 'l': l})

    # Inserts the 2 extra instances of openTableRed so len(colorMatrix) is divisible by 4
    variationMatrix.insert(50, {'h': 0, 'c': 0, 'l': 0})
    variationMatrix.insert(151, {'h': 0, 'c': 0, 'l': 0})

    return variationMatrix

# Returns a given rgb value as its corresponding hex value
def toHex(r,g,b):
    return ("#%02X%02X%02X" % (r, g, b)).lower()

def createCSV():
    import csv
    with open('colors2.csv', 'w') as csvfile:
        fieldnames = ['L', 'a', 'b', 'c', 'h', 'r', 'g', 'b2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        colorDict = getOpenTableDict()
        writer.writeheader()

        for row in colorDict:
            writer.writerow(row)