from __future__ import print_function

import os
import sys

def totalNoPalindromSubstr(text,length):
    T = "#".join("^{}$".format(text))
    n = len(T)
    P = [0]*n
    total_no_palindrom_substr = 0
    new_total = 0
    C = R = 0
    for i in range(1,n-1):
        if(R > i):
            P[i] = min(R-i,P[2*C - i])
        else:
            P[i] = 0
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            # print(i,P)
            P[i]+=1
        total_no_palindrom_substr += P[i]//2

        if i+P[i] > R:
            C,R = i, i + P[i]
            # new_total = 


    return total_no_palindrom_substr


if __name__ == "__main__":
    n = input()
    for i in range(int(n)):
        length_of_str = int(input())
        text = input()
        print(totalNoPalindromSubstr(text,length_of_str))
