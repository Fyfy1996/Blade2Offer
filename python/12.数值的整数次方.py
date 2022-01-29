# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:46:56 2022

@author: fanyong
"""
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。


def Power(base, exponent):
    if base == 0:
        return 0
    if_reverse = False
    if exponent < 0:
        if_reverse = True
    re = 1
    for i in range(exponent):
        re *= base
    if if_reverse:
        re /= 1
    return re

print(Power(1e-11,30))