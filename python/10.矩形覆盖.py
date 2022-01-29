# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:36:04 2022

@author: fanyong
"""

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？


def RectangleCover(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    else:
        n_2, n_1 = 1,2
        for i in range(3,n+1):
            tmp = n_2 + n_1
            n_2 = n_1
            n_1 = tmp
    return tmp

print(RectangleCover(4))