from __future__ import print_function

import os
import sys

def log2n(n):
    return 1 + log2n(n/2) if(n>1) else 0

def pow(x,n):
    if n == 0:
        return 1
    tmp = pow(x,y/2)
    if(x%2 == 0):
        return tmp*tmp
    else:
        return x*tmp*tmp

def findLongestEvenlengthSubstring(s):
    n = len(s)
    D = [[0 for i in range(n)] for j in range(n)]
    log_n = log2n(n)
    length_of_longest_even_string = 0
    for i in range(0,n):
        D[i][i] = int(s[i])
        if (i > 0) and (D[i][i] == D[i-1][i-1]):
            length_of_longest_even_string = 1


    for length in range(2,(n//2)+1):
        for i in range(0,n-length+1):
            j = i + length - 1
            D[i][j] = D[i][j-1] + int(s[j])
            if(i >= length) and (D[i][j] == D[i-length][j-length]):
                length_of_longest_even_string = length

            # print(i,j,D[i][j-1],int(s[j]),D[i][j])
    # print(D,length_of_longest_even_string)
    return length_of_longest_even_string*2

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(findLongestEvenlengthSubstring(input()))
