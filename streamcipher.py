#python cipher.py e key.txt plaintext.txt 
#python cipher.py d key.txt ciphertext.txt 

import time
# from bruteForce import char

# The first function is the Key Setup phase, which uses a user-supplied secret key to initialize a permutation S that the cipher needs.
def KSA(key):
    keyLength = len(key)
    K = list(range(256))

    j = 0
    for i in range(256):
        j = (j + K[i] + key[i % keyLength]) % 256
        K[i], K[j] = K[j], K[i]

    return K

# The second function uses the permutation to generate a byte stream that can be XOR-ed with the plaintext (ciphertext) to encrypt (decrypt) it.
def PRGA(K):
    i = 0
    j = 0

    while True:
        i = (i + 1) % 256
        j = (j + K[i]) % 256
        K[i], K[j] = K[j], K[i]
        S = K[(K[i] + K[j]) % 256]
        yield S

def streamCipher(key):
    S = KSA(key)
    return PRGA(S)



if __name__ == '__main__':
    import sys

    def convert_to_bytes(s):
        return bytes([ord(c) for c in s])

    words = []
    dict = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

    with open(sys.argv[2], 'r') as keyfile:
        for line in keyfile:
            if (len(line) == 5):
                words.append(line.lower())

        for i in range(0, len(words)):
            words[i] = words[i][:-1]
            key = convert_to_bytes(words[i])
        # key = convert_to_bytes(keyfile.read())

    #print(key)
            keystream = streamCipher(key)

            with open(sys.argv[3], 'r') as inputfile:
                if sys.argv[1] == 'e':  #encryption
                    plaintext = inputfile.read() #Read the plaintext as a string from the inputfile
                    output_ciphertext = []
                    
                    start = time.time()

                    for c in plaintext:
                        output_ciphertext.append(ord(c) ^ next(keystream)) #Turn each character from the plaintext string to an integer. XOR it with the next integer from the keystream to encrypt it.
                        
                    end = time.time()

                    time = (end - start)

                    print(bytes(output_ciphertext).hex(), file=sys.stdout, end='') #Replace sys.stdout if you want to write output to a file
                    
                    
                    print()
                    print("Time taken in seconds: ", time)
                
                elif sys.argv[1] == 'd': #decryption           
                    ciphertext = inputfile.read() #Read the ciphertext as a string from the inputfile
                    output_plaintext = []
                    
                    for c in bytes.fromhex(ciphertext): #Convert the ciphertext hex string into a sequence of integers (https://docs.python.org/3/library/stdtypes.html#bytes.fromhex)
                        newtext = output_plaintext.append(chr(c ^ next(keystream))) #XOR each ciphertext integer c with the next integer from the keystream to decrypt it. Turn the resulting integer to a character.
                        print(newtext)
                        for i in newtext:
                            for k in i:
                                if k not in dict:
                                    continue
                                else:
                                    newtext = print(''.join(output_plaintext), file=sys.stdout, end='') #Replace sys.stdout if you want to write output to a file

                else:
                    print("Unknown opcode. Opcode should be 'e' for encryption or 'd' for decryption.", file=sys.stderr)
