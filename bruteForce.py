#python .\bruteForce.py .\ciphertexts.txt

#STEP ONE: ITERATE THROUGH DICTIONARY
#STEP TWO: FILTER TO 4 LETTER WORDS
#STEP THREE: .lower() all 4 letter words
#STEP FOUR: Use all 4 letter words as key in decryption in streamcipher.py
import sys

words = []

wordLength = int(input("Enter length of word: "))

file = open("words.txt", "r")


for line in file:
    if (len(line) == (wordLength + 1)):
        words.append(line.lower())

#Remove the \n that appears at the end of each word
for i in range (0, len(words)):
    words[i] = words[i][:-1]

#testing
print(words)



input_file = open(sys.argv[1])
input_str = input_file.read()


for i in words:
    key = i


    no_of_itr = (len(input_str))
    output_str = ""

    for i in range(no_of_itr):
        current = input_str[i]
        current_key = key[i%len(key)]
        output_str += chr(ord(current) ^ ord(current_key))

    print("Heres the output: ", output_str)

# file.close()

