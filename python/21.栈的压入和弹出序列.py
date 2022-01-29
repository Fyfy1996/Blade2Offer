# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:44:09 2022

@author: fanyong
"""


def IsPopOrder(pushV, popV):
    stack = []
    i = 0
    j = 0
    while i < len(pushV):
        stack.append(pushV[i])
        while j < len(popV) and stack[-1] == popV[j]:
            j += 1
            _=stack.pop()
        i += 1
    return True if len(stack) == 0 else False

print(IsPopOrder([1,2,3,4,5], [4,3,5,1,2]))

print(IsPopOrder([1,2,3,4,5], [4,5,3,2,1]))