from __future__ import print_function

import os
import sys

def totalNoPallindromSubstr(text,length):
    text_list = list(text);
    reverse_text_list = text_list[::-1];
    twod_list = []
    total_no_pallindrom_substr = 0
    for i in range(length):
        oned_list = [0 for x in range(length)]
        twod_list.append(oned_list)
        for j in range(length):
          if text_list[j] == reverse_text_list[i]:
            if i>0 and j>0:
              twod_list[i][j] = 1+twod_list[i-1][j-1]
              if i==(length-1) or j==(length-1):
                if i==length-1 and j+1 == twod_list[i][j] or j==length-1 and i+1 == twod_list[i][j]:
                  total_no_pallindrom_substr += int((twod_list[i][j])/2)
                
            else:
              twod_list[i][j] = 1
          else:
            if i>0 and j>0:
                if i - twod_list[i-1][j-1]  == length - j :
                  total_no_pallindrom_substr += int(twod_list[i-1][j-1]/2)
    return total_no_pallindrom_substr 


if __name__ == "__main__":
    n = input()
    for i in range(int(n)):
        length_of_str = int(input())
        text = input()
        print(totalNoPallindromSubstr(text,length_of_str))
