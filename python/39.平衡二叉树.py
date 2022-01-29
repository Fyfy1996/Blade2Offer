# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:50:17 2021

@author: fanyong
"""
from nodes import TreeNode
t0 = TreeNode(1)
t1 = TreeNode(3)
t2 = TreeNode(4)
t3 = TreeNode(2)
t4 = TreeNode(4)
t5 = TreeNode(1)
t6 = TreeNode(2)
t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.right = t6
t2.left = t5


cnt = 0
def TreeDepth(tree):
    global cnt
    cnt += 1
    if tree == None:
        return 0
    left = TreeDepth(tree.left)
    right= TreeDepth(tree.right)
    return max(left, right)+1

def IsBalancedTree(tree):
    if tree == None:
        return True
    left = IsBalancedTree(tree.left)
    right= IsBalancedTree(tree.right)
    if left and right:
        l_p = TreeDepth(tree.left)
        r_p = TreeDepth(tree.right)
        if abs(l_p-r_p) <= 1:
            return True
        else:
            return False
    else:
        return False


print(IsBalancedTree(t0))        