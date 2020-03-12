import numpy as np


def codeToBinary(fileIn):
    translate_dict = {
        'A': 0, 'Q': 16, 'g': 32, 'w': 48,
        'B': 1, 'R': 17, 'h': 33, 'x': 49,
        'C': 2, 'S': 18, 'i': 34, 'y': 50,
        'D': 3, 'T': 19, 'j': 35, 'z': 51,
        'E': 4, 'U': 20, 'k': 36, '0': 52,
        'F': 5, 'V': 21, 'l': 37, '1': 53,
        'G': 6, 'W': 22, 'm': 38, '2': 54,
        'H': 7, 'X': 23, 'n': 39, '3': 55,
        'I': 8, 'Y': 24, 'o': 40, '4': 56,
        'J': 9, 'Z': 25, 'p': 41, '5': 57,
        'K': 10, 'a': 26, 'q': 42, '6': 58,
        'L': 11, 'b': 27, 'r': 43, '7': 59,
        'M': 12, 'c': 28, 's': 44, '8': 60,
        'N': 13, 'd': 29, 't': 45, '9': 61,
        'O': 14, 'e': 30, 'u': 46, '+': 62,
        'P': 15, 'f': 31, 'v': 47, '/': 63
    }
    with open(fileIn, "r") as fi, \
            open("6bitDecoded.txt", "w") as fo:
        line = fi.readline()
        values = [translate_dict[sym] for sym in line]
        for i in range(0, len(values)):
            h = format(values[i], '06b')
            fo.write(h)


def binaryToText(fileOut):
    with open("6bitDecoded.txt", "r") as fi, \
            open(fileOut, "w") as fo:
        line = fi.readline()
        as8Bit = []
        outSymbols = []
        for i in range(0, len(line), 8):
            if i + 8 < len(line):
                as8Bit.append(line[i:i + 8])
            else:
              #  as8Bit.append(line[i:len(line)])
                break
        print(as8Bit)
        for i in as8Bit:
            outSymbols.append(bin2dec(i))
        print(outSymbols)
        for i in outSymbols:
            fo.write(chr(i))


def binaryToText_6bit(fileOut):
    tablica = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    with open("8bitDecoded.txt", "r") as fi, \
            open(fileOut, "w") as fo:
        line = fi.readline()
        list = []
        newDec = []
        for i in range(0, len(line), 6):
            if i + 6 < len(line):
                list.append(line[i:i + 6])
            else:
                list.append(line[i:len(line)])
                break
        for i in list:
            newDec.append(bin2dec(i))
        for i in newDec:
            fo.write(tablica[i])


def textToBinary_8bit(fileInPath):
    with open(fileInPath, "r") as fi, \
            open("8bitDecoded.txt", "w") as fo:
        line = fi.readline()
        lineCounter = 1
        asciiListOfLines = []
        while line:
            asciiListOfLines.append([ord(c) for c in line])
            line = fi.readline()
            lineCounter += 1
        asciiList = np.sum(asciiListOfLines, 0)
        for i in range(0, len(asciiList)):
            h = format(asciiList[i], '08b')
            fo.write(h)


def bin2dec(b):
    number = 0
    counter = 0
    for i in b[::-1]:  # Iterating through b in reverse order
        number += int(i) * (2 ** counter)
        counter += 1

    return number


def encode():
    codeToBinary("code.txt")
    binaryToText("output.txt")


def decode():
    textToBinary_8bit("input.txt")
    binaryToText_6bit("code.txt")


decode()
encode()
