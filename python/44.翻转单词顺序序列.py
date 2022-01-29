# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:38:09 2022

@author: fanyong
"""


def RotateList(ls):
    start,end = 0,len(ls)-1
    while start < end:
        ls[start], ls[end] = ls[end], ls[start]
        start += 1
        end -= 1
        
def RotateStr(string):
    ls = string.split(" ")
    RotateList(ls)
    return " ".join(ls)

print(RotateStr("student. a am I"))
        
        
        