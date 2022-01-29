# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:27:55 2022

@author: fanyong
"""
def Str2Int(string):
    length = len(string)
    if length == 0:
        return 0
    
    
    positive = 1
    if string[0] == "-":
        positive = -1
    
    start = 0
    if string[0] in ["+", "-"]:
        start = 1
    num = 0
    for i in range(length-1,start-1,-1):
        if string[i] <= '9' and string[i] >= '0':
            num += eval(string[i])*10**(length-i-1)
        else:
            num = 0
            break
    return num*positive


print(Str2Int("+123132"))

print(Str2Int("+1231dasd"))