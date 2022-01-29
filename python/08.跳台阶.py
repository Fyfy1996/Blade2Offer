# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:23:16 2022

@author: fanyong
"""
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# n-1级台阶和n-2级台阶的跳法之和

def JumpSteps(n):
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

print(JumpSteps(4))
    