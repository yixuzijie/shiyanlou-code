#!/usr/bin/env python3
x = float(input("Enter the value of x:"))
term = n = 1
result = 1.0
while n <= 100:
    term *= x/n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Time = {} and Sum = {}".format(n,result))
