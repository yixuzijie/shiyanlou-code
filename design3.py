#!/usr/bin/env python3
row = int(input("enter the number of rows:"))
n = row
while n > 0:
    print(" "*(row-n),"*"*n)
    n -= 1
