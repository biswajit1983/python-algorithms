from __future__ import print_function

import os
import sys

def longestPalindrome(s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        total_no_palindrom_substr = 0
        # print(T)
        for i in range (1, n-1):
            k = 0
            print(list(T))
            print(P)
            print("Start:","C=",C,"R=",R,"i=",i,"iMirror=",2*C-i)
            if (R > i):
                print("R > i",R-i,P[2*C - i])
                P[i] = min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            else:
                P[i] = 0

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
                k = k+1
                print(i,k,P)

            total_no_palindrom_substr = total_no_palindrom_substr + P[i]//2

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
            print("END:","C=",C,"R=",R,"i=",i,"iMirror=",2*C-i)

        # Find the maximum element in P.
        # print(enumerate(P))
        # print((n, i) for i, n in enumerate(P))
        # maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        # print(s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2])
        return total_no_palindrom_substr

if __name__ == "__main__":
    n = input()
    for i in range(int(n)):
        length_of_str = int(input())
        text = input()
        print(longestPalindrome(text))
