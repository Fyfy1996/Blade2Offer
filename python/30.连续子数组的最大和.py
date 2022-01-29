# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:17:03 2021

@author: fanyong
"""
arr = [1,-2,3,10,-4,7,2,-5]

def MaxSubArrSum(arr):
    acc_sum = 0
    max_sum = 0
    if len(arr) == 0:
        return 0
    for num in arr:
        acc_sum += num
        if acc_sum < 0:
            acc_sum = 0
        if max_sum < acc_sum:
            max_sum = acc_sum
    return max_sum

print(MaxSubArrSum(arr))