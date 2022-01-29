# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:12:09 2021

@author: fanyong
"""
from nodes import TreeNode
t0 = TreeNode(1)
t1 = TreeNode(3)
t2 = TreeNode(3)
t3 = TreeNode(2)
# t4 = TreeNode(4)
# t5 = TreeNode(4)
t6 = TreeNode(2)

t0.left = t1
t0.right = t2
t1.left = t3
# t1.right = t4
t2.right = t6
# t2.left = t5

def recursiveTree(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.x == right.x:
        return recursiveTree(left.left, right.right) and recursiveTree(left.right, right.left)
    return False

def IsSymmetrical(pRoot):
    # write code here
    if not pRoot:
        return True
    return recursiveTree(pRoot.left, pRoot.right)
 
print(IsSymmetrical(t0))