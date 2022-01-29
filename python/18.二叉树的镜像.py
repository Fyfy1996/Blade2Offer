# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:59:30 2021

@author: fanyong
"""
from nodes import TreeNode, Print_PreOrder


def MirrorTree(tree):
    if tree == None:
        return tree
    left = tree.left
    right = tree.right
    
    tree.left = right
    tree.right = left
    
    tree.left = MirrorTree(tree.left)
    tree.right = MirrorTree(tree.right)
    return tree

t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t0.left = t1
t0.right= t2
t1.left = t3
t1.right=t4
print(Print_PreOrder(t0))

print(Print_PreOrder(MirrorTree(t0)))