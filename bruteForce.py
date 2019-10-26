#key = 4 characters long, lowercase letters only

#try every possible combination of 4 characters as the key

#STEP ONE: ITERATE THROUGH DICTIONARY
#STEP TWO: FILTER TO 4 LETTER WORDS
#STEP THREE: .lower() all 4 letter words
#STEP FOUR: Use all 4 letter words as key in decryption in streamcipher.py
import sys

words = []

wordLength = int(input("Enter length of word: "))

file = open("words.txt", "r")

def characters4():
    for line in file:
        if (len(line) == (wordLength + 1)):
            words.append(line.lower())

    #Remove the \n that appears at the end of each word
    for i in range (0, len(words)):
        words[i] = words[i][:-1]

    print(words)
    return words

characters4()
# file.close()

