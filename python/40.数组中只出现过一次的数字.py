# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:23:13 2021

@author: fanyong
"""
arr1 = [1,2,3,1,2,3,4,5,5,6]


def OneTimeNum(arr):
    if len(arr)<= 1:
        return []
    xor = 0
    for i in arr:
        xor ^= i
    idx = GetBitIndex(xor)
    i = 0
    num1,num2 = 0,0
    for i in arr:
        if BitIs1(i, idx) == 1:
            num1 ^= arr[i]
        else:
            num2 ^= arr[i]
    return num1, num2
    
    
    
    
def GetBitIndex(num):
    i = 0
    while num & 1 == 0:
        i += 1
        num = num >> 1
    return i


def BitIs1(num, idx):
    num >>= idx
    return num & 1


print(OneTimeNum(arr1))