from __future__ import print_function

import os
import sys

def isSquare(k):
    return round(k**0.5)**2 == k

def countSqaures(n):
    return len(list(filter(isSquare,range(1,n))))
    # print(lst,len(lst))
    # return 0


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        print(countSqaures(m))
