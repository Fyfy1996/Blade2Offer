# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:11:26 2021

@author: fanyong
"""


def MoreThanHalfNum(arr):
    cnt = 1
    prev = arr[0]
    for i in range(1,len(arr)):
        if prev == arr[i]:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            prev = arr[i]
            cnt = 1
    cnt = 0
    for i in arr:
        if i == prev:
            cnt += 1
    return prev if cnt >= len(arr) // 2 else 0 


print(MoreThanHalfNum([1,2,2,4,2,1,2,5,6,1,1,1]))