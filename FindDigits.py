#!/usr/bin/env python3
import os
import sys

def digi(cont):
    b = ''
    for i in cont:
        if i.isdigit() == True:
            b = b + i
    return b
file = '/tmp/String.txt'
if __name__ == "__main__":
    if os.path.exists(file):
        text = open(file)
        cont = text.read()
        print(digi(cont))
        text.close()
    else:
        sys.exit(-1)
    sys.exit(0)
