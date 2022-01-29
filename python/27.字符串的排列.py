# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:01:08 2022

@author: fanyong
"""
def Permutation(string):
    pass
    

def Permute(front_str, end_str):
    if end_str == []:
        print(front_str+end_str)
    for i,v in enumerate(end_str):
        front_new = front_str+[v]
        end_new = end_str.copy()
        _=end_new.pop(i)
        Permute(front_new, end_new)

        
Permute([],["a", "b", "c"])