from __future__ import print_function

import os
import sys


def allPalindromeSubstringsInARange(s,i,j):
    T = '#'.join("^{}$".format(s[i:j+1]))
    # print(T)
    n = len(T)
    P = [0]*n
    C = R = 0
    total_p_substr = 0

    for i in range(1,n-1):
        if R > i:
            P[i] = min(R - i, P[2*C - i])
        while(T[i + 1 + P[i]] == T[i - 1 - P[i]]):
            P[i] += 1
        if i+P[i] > R:
            C,R = i, i+P[i]
            # print(C,i,P)
        boundary = P[i]
        left = (C - boundary)//2
        right = (C + boundary)//2
        while boundary!=0:
            tmp = s[left:right]
            # print(tmp)
            if tmp:
                total_p_substr += 1
            boundary = boundary // 2
            left += 1
            right -= 1
    return total_p_substr

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        length = int(input())
        str = input()
        q_range = input()
        q_range_start = int(q_range.split(' ')[0])
        q_range_end = int(q_range.split(' ')[1])
        if q_range_start < q_range_end:
            print(allPalindromeSubstringsInARange(str,q_range_start,q_range_end))
        else:
            print(allPalindromeSubstringsInARange(str,q_range_end,q_range_start))
