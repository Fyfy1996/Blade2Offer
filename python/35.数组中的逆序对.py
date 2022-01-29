# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:37:39 2021

@author: fanyong
"""
arr = [7,5,6,1,3,2]

def CntAB(arr1, arr2):
    cnt = 0
    i,j = 0,0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            res.append(arr1[i])
            cnt += len(arr2) - j
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i < len(arr1):
        res += arr1[i:]
    if j < len(arr2):
        res += arr2[j:]
    return res, cnt
            
# print(CntAB([5,3,1], [4,2,1]))

def MergeCnt(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_cnt = MergeCnt(arr[:mid])
    right,r_cnt = MergeCnt(arr[mid:])
    all_ls, mid_cnt = CntAB(left, right)
    return all_ls, l_cnt+r_cnt+mid_cnt

print(MergeCnt(arr))