# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:11:17 2021

@author: fanyong
"""


def ReorderArray(arr):
    border = -1
    for idx in range(len(arr)):
        if arr[idx] % 2:
            border += 1
            arr.insert(border, arr.pop(idx))
    return arr

print(ReorderArray([2,3,1,5,8,5]))