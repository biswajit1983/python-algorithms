from __future__ import print_function

import os
import sys


def countAllDistinctPalindromeSubstrings(s):
    total_no_palindrome_substr = 0
    map = {}
    T = ('#').join("^{}$".format(s))
    n = len(T)
    P = [0]*n
    C = R = 0
    # print(list(T))
    for i in range(1,n-1):
        if R > i :
            P[i] = min(R - i, P[2*C - i])
        while(T[i + 1 + P[i]] == T[i - 1 - P[i]]):
            P[i] += 1


        if i+P[i] > R :
            C,R = i, i+P[i]
            # print(P,i,C)
        boundary = P[i]
        left = (C - boundary)//2
        right = (C + boundary)//2
        while boundary != 0:
            tmp = s[left:right]
            # print(C,boundary,len(s),len(T),(C-boundary)//2,(C+boundary)//2,s[(C - boundary)//2],s[(C + boundary)//2-1],tmp)
            # if len(tmp) > 1:
            if tmp:
                map[tmp] = 1
            boundary = boundary//2
            left += 1
            right -= 1
    # print(map)
    total_no_palindrome_substr = len(map)
    return total_no_palindrome_substr

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(countAllDistinctPalindromeSubstrings(input()))
