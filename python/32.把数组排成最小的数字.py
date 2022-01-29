# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:18:18 2021

@author: fanyong
"""

import functools

arr = [3,12,4,28,5,6]

def PrintMinNum(arr):
    if len(arr) == 0:
        return ""
    compare = lambda a,b: 1 if str(a)+str(b) > str(b)+str(a) else -1
    min_str = sorted(arr, key=functools.cmp_to_key(compare))
    return "".join([str(i) for i in min_str])

print(PrintMinNum(arr))