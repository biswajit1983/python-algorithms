from __future__ import print_function

import os
import sys

def longestPalindrome(s,n):
    D = [[0 for i in range(n)] for j in range(n)]
    P = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        P[i][i] = True
    for i in range(n-1):
        if(s[i] == s[i+1]):
            P[i][i+1] = True
            D[i][i+1] = 1
    for d in range(2,n):
        for i in range(0,n-d):
            j = i+d
            if s[i]==s[j] and P[i+1][j-1]:
                P[i][j] = True
            if P[i][j]:
                D[i][j] = D[i][j-1] + D[i+1][j] + 1 - D[i+1][j-1]
                # print("Here",i,j,D[i][j],D[i][j-1],D[i-1][j])
            else:
                D[i][j] = D[i][j-1] + D[i+1][j] - D[i+1][j-1]
            # print(j,P,D)
    return D[0][n-1]

if __name__ == "__main__":
    n = input()
    for i in range(int(n)):
        length_of_str = int(input())
        text = input()
        print(longestPalindrome(text,length_of_str))
