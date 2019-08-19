#!/usr/bin/env python3
n = int(input('enter the value of n of nxn:'))
print('The matrix A:')
A = []
for i in range(n):
    A.append([int(x) for x in input().split()])
print('The matrix B:')
B = []
for j in range(n):
    B.append([int(x) for x in input().split()])
C = []
for i in range(n):
    for j in range(n):
        C.append(A[i][j]*B[i][j])
print('After matrix multiplication')
print('-'*7*n)
for i in range(n):
    for j in range(n):
        print(str(C[i*n+j]).rjust(5),end='')
    print()
print('-'*7*n)


for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)
