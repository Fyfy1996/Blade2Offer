# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:49:36 2021

@author: fanyong
"""
matrix = [[1,3,4,9],
          [2,4,5,10],
          [4,7,8,11],
          [6,9,10,12]]

def SearchNum(mat, num):
    length = len(matrix) - 1
    width = len(matrix[0]) - 1
    i,j = 0,width
    while i <= length and j >= 0:
        if mat[i][j] == num:
            return True
        elif mat[i][j] > num:
            j -= 1
        elif mat[i][j] < num:
            i += 1
    return False

print(SearchNum(matrix,6))