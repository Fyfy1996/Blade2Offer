# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 16:30:56 2022

@author: fanyong
"""
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。


def MultiplyArray(A):
    B = [1]
    tmp = 1
    length = len(A)
    for i in range(1,len(A)):
        tmp *= A[i-1]
        B.append(tmp)
    
    tmp = 1
    for i in range(len(A)-2, -1, -1):
        tmp *= A[i+1]
        B[i] *= tmp
    return B

array = MultiplyArray([1,2,3,4,5])
        