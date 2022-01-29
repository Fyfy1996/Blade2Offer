# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:46:02 2021

@author: fanyong
"""
arr = [2,3,4,4,5]


def FindMinInRoatateArray(array):
    if len(array) == 0:
        return 0
    p, q = 0, len(array)-1
    while q > p:
        if q - p == 1:
            mid = q
            break
        mid = p + (p-q) //2
        if array[mid] >= array[p]:
            p = mid
        elif array[mid] < array[p]:
            q = mid
    return array[mid]

print(FindMinInRoatateArray(arr))
            