# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:43:46 2022

@author: fanyong
"""



def NumberOf1(n):
    cnt = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt

print(NumberOf1(15))