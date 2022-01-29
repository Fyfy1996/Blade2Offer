# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:51:52 2021

@author: fanyong
"""

arr = [7,7,7,7,7,7,7]




def GetHead(arr, num):
    if num < arr[0] and num > arr[-1]:
        return -1
    if num == arr[0]:
        return 0
    i,j = 0, len(arr)-1
    while i < j-1:
        mid = (i+j)//2
        if num <= arr[mid]:
            j = mid
        else:
            i = mid
    return i+1

def GetTail(arr, num):
    if num < arr[0] and num > arr[-1]:
        return -1
    if num == arr[-1]:
        return len(arr)-1
    i,j = 0, len(arr)-1
    while i < j-1:
        mid = (i+j)//2
        if num < arr[mid]:
            j = mid
        else:
            i = mid
    return j-1
    

def NumCnt(arr, num):
    tail = GetTail(arr, num)
    head = GetHead(arr, num)
    # print(head, tail)
    return tail-head+1
    
    

print(NumCnt(arr,7))