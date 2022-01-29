# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:44:56 2021

@author: fanyong
"""

arr = [1,3,2,0,2,5,3]

def DuplicateNum(arr):
    i = 0
    while i <= len(arr)-1:
        idx_num = arr[i]
        if i == idx_num:
            i += 1
        else:
            if idx_num == arr[idx_num]:
                return idx_num
            else:
                arr[i], arr[idx_num] =  arr[idx_num],arr[i]
    return None

print(DuplicateNum(arr))