# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:51:50 2022

@author: fanyong
"""






def PrintMatrix(mtx):
    length = len(mtx)
    width = len(mtx[0])
    result = []
    if length == 0 or width == 0:
        return
    left,right,up,bot = 0,width-1,0,length-1
    while left <= right and up <= bot:
        for i in range(left, right):
            result.append(mtx[up][i])
        for j in range(up, bot):
            result.append(mtx[j][right])
        for i in range(right, left,-1):
            result.append(mtx[bot][i])
        for j in range(bot,up,-1):
            result.append(mtx[j][left])
        left += 1
        right -= 1
        up += 1
        bot -= 1
    return result


matrix = [[1,2],
          [2,3],
          [5,6]]
print(PrintMatrix(matrix))
            