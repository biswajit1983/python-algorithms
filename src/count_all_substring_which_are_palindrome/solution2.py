from __future__ import print_function

import os
import sys

def totalNoPalindromSubstr(text,length):
    text_list = list(text);
    # reverse_text_list = text_list[::-1];
    twod_list = []
    total_no_palindrom_substr = 0
    for i in range(length)[1:]:
        middle = i
        start = i-1
        end = i+1
        # print(start,middle,end)
        if text_list[start] == text_list[middle]:
            total_no_palindrom_substr+=1
            # print("T0",text[start:middle+1],start,middle)
            t_start = start - 1
            t_end = end
            while t_start >= 0 and t_end <= length - 1:
                if text_list[t_start] == text_list[t_end]:
                    # print("T4",text[t_start:t_end+1],t_start,t_end)
                    total_no_palindrom_substr+=1
                    t_start-=1
                    t_end+=1
                else:
                    break

        if end <= length-1 and text_list[start] == text_list[end]:
            # print("T1",text[start:end+1],start,end)
            total_no_palindrom_substr+=1
            t_start = start - 1
            t_end = end + 1
            while t_start >= 0 and t_end <= length -1:
                if text_list[t_start] == text_list[t_end]:
                    # print("T2",text[t_start:t_end+1],t_start,t_end)
                    total_no_palindrom_substr+=1
                    t_start-=1
                    t_end+=1
                else:
                    break
        # if text_list[middle] == text_list[end]:
        #     print("T3",text[middle:end+1],middle,end)
        #     total_no_palindrom_substr+=1
        #     t_end = end + 1
        #     t_start = start
        #     while t_start >= 0 and t_end <= length - 1:
        #         if text_list[t_start] == text_list[t_end]:
        #             print("T4",text[t_start:t_end+1],t_start,t_end)
        #             total_no_palindrom_substr+=1
        #             t_start-=1
        #             t_end+=1
        #         else:
        #             break
    return total_no_palindrom_substr


if __name__ == "__main__":
    n = input()
    for i in range(int(n)):
        length_of_str = int(input())
        text = input()
        print(totalNoPalindromSubstr(text,length_of_str))
