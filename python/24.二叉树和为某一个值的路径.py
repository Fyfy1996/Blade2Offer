# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:26:57 2021

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

def FindPath(tree, target):
    if tree == None:
        return []
    if tree.left == None and tree.right == None and tree.x == target:
        return [[tree.x]]
    left = FindPath(tree.left, target-tree.x)
    right= FindPath(tree.right, target-tree.x)
    res = []
    for i in left+right:
        res.append([tree.x] + i)
    return res

print(FindPath(t0,6))
        