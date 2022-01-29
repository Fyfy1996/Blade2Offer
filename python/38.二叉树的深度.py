# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:02:30 2021

@author: fanyong
"""

from nodes import TreeNode
t0 = TreeNode(1)
t1 = TreeNode(3)
t2 = TreeNode(4)
t3 = TreeNode(2)
# t4 = TreeNode(4)
t0.left = t1
t0.right= t2
t1.left = t3
# t1.right=t4


def TreeDepth(tree):
    if tree == None:
        return 0
    left = TreeDepth(tree.left)
    right= TreeDepth(tree.right)
    return max(left, right)+1

print(TreeDepth(t0))