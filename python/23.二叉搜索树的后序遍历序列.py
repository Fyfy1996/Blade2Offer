# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:17:50 2022

@author: fanyong
"""

# def VerifySquenceOfBST(sequence):
#     # write code here
#     if not len(sequence):
#         return False
#     if len(sequence) == 1:
#         return True
#     length = len(sequence)
#     root = sequence[-1]
#     i = 0
#     while sequence[i] < root:
#         i = i + 1
#     k = i
#     for j in range(i, length-1):
#         if sequence[j] < root:
#             return False
#     left_s = sequence[:k]
#     right_s = sequence[k:length-1]
#     left, right = True, True
#     if len(left_s) > 0:
#         left = VerifySquenceOfBST(left_s)
#     if len(right_s) > 0:
#         right = VerifySquenceOfBST(right_s)
#     return left and right


def VerifyBST(seq, begin, end):
    if len(seq) == 0:
        return False
    
    root = seq[end]
    
    for i in range(begin, end+1):
        if seq[i] > root:
            break
    
    for j in range(i, end+1):
        if seq[j] < root:
            return False
    
    left, right = True, True
    if i > begin:
        left = VerifyBST(seq, begin, i-1)
    
    if i < end - 1:
        right = VerifyBST(seq, i, end-1)
        
    return left and right


print(VerifyBST([5,7,6,9,11,10,8], 0, 6))
    
    
    

