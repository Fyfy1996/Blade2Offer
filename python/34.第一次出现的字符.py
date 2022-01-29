# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:08:54 2022

@author: fanyong
"""
def FirstOnceChar(string):
    cnts = {}
    for i in string:
        cnts[i] = cnts.get(i,0) + 1
    
    for i,v in enumerate(string):
        if cnts[v] == 1:
            return i
    return -1

print(FirstOnceChar("aabbccddffttahjjjl"))