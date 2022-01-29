# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:27:38 2022

@author: fanyong
"""
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 1,2,3, ** n-1级台阶和n-2级台阶的跳法之和

def HentaiJumpSteps(n):
    if n <= 2:
        return n
    else:
        return 2**(n-1)
    
print(HentaiJumpSteps(10))