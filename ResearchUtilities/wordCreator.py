import enchant
from random import randint

dict = enchant.Dict("en_US")
vowels = ['a', 'e', 'i', 'o', 'u']
rounded = ['b', 'd', 'g', 'l', 'm', 'n', 'p', 's']
spiky = ['k', 't', 'v', 'z']

def main():
    '''
    print("########## CVCV ##########")
    createVaryingVowelWords(spiky)
    print("\n")
    createVaryingConsonantWords(spiky)
    '''
    randomWords(['k', 't', 'v', 'z', 'a', 'e', 'i', 'o', 'u'], 5, 100)

def createVaryingVowelWords(consonants):
    for i in range(0, 4):
        for j in range(i + 1, 5):
            print("# Varying Vowel (%s & %s)" % (vowels[i], vowels[j]))
            for consonant in consonants:
                word1 = consonant + vowels[i] + consonant + vowels[j]
                word2 = consonant + vowels[j] + consonant + vowels[i]

                # Won't print the word pair if either exists in the English dictionary
                if dict.check(word1) or dict.check(word2):
                    continue
                else:
                    print('["%s", "%s"],' %(word1, word2))

def createVaryingConsonantWords(consonants):
    for i in range(0, len(consonants) - 1):
        for j in range(i + 1, len(consonants)):
            print("# Varying Consonant (%s & %s)" % (consonants[i], consonants[j]))
            for vowel in vowels:
                word1 = consonants[i] + vowel + consonants[j] + vowel
                word2 = consonants[j] + vowel + consonants[i] + vowel

                # Won't print the word pair if either exists in the English dictionary
                if dict.check(word1) or dict.check(word2):
                    continue
                else:
                    print('["%s", "%s"],' % (word1, word2))

def randomWords(letters, wordLength, numWords):
    for i in range(0, numWords):
        word = ""
        for j in range(0, wordLength):
            word += letters[randint(0, len(letters) - 1)]
        print(word)

main()