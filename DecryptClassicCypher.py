# Python Version 2.7 - Cathal Murphy B00095643
import sys

print(sys.argv[1] + " decrypting " + sys.argv[2])

if str(sys.argv[1]) == "rot5":  # rot 5 0-9 digit rotation

    toBeEncrypt = []
    for x in sys.argv[2]:
        toBeEncrypt.append(x)
    rotation = 1
    while rotation != 10:
        term = -1
        for y in toBeEncrypt:
            term = term + 1
            newLetter = ord(y) + 1
            if newLetter > ord('9'):
                newLetter = newLetter - 10

            toBeEncrypt[term] = chr(newLetter)
        print("Key = " + str(rotation) + " " + str(toBeEncrypt))
        rotation = rotation + 1


if str(sys.argv[1]) == 'rot13':  # over alpha

    toBeEncrypt = []
    for x in sys.argv[2]:
        toBeEncrypt.append(x)

    rotation = 1
    while rotation != 26:
        term = -1
        for y in toBeEncrypt:
            term = term + 1
            newLetter = ord(y) + 1
            if newLetter > ord('z'):
                newLetter = newLetter - 26

            toBeEncrypt[term] = chr(newLetter)
        print("Key = " + str(rotation) + " " + str(toBeEncrypt))
        rotation = rotation + 1

if str(sys.argv[1]) == 'rot47':  # put permutaions for keys

    toBeEncrypt = []
    for x in sys.argv[2]:
        toBeEncrypt.append(x)

    rotation = 1
    while rotation != 93:
        term = -1
        for y in toBeEncrypt:
            term = term + 1
            newLetter = ord(y) + 1
            if newLetter > ord('~'):
                newLetter = newLetter - 94

            toBeEncrypt[term] = chr(newLetter)
        print("Key = " + str(rotation) + " " + str(toBeEncrypt))
        rotation = rotation + 1


