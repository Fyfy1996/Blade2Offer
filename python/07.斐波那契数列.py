# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:12:02 2022

@author: fanyong
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        n_2, n_1 = 0,1
        for i in range(2,n+1):
            tmp = n_2 + n_1
            n_2 = n_1
            n_1 = tmp
    return tmp

print(fib(10))
    