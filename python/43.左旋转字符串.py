# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:17:07 2022

@author: fanyong
"""
def RotateList(ls, start, end):
    while start < end:
        ls[start], ls[end] = ls[end], ls[start]
        start += 1
        end -= 1
        
        
def ROL(ls, num):
    length = len(ls)
    num = num % length -1
    RotateList(ls, 0, num)
    # print(ls)
    RotateList(ls, num+1, length-1)
    # print(ls)
    RotateList(ls, 0, length-1)
    # print(ls)
    

ll = [i for i in "abcdefg"]
ROL(ll,2)

print(ll)