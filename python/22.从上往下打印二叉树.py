# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:03:30 2021

@author: fanyong
"""
from nodes import TreeNode, Print_PreOrder
t0 = TreeNode(1)
t1 = TreeNode(3)
t2 = TreeNode(4)
t3 = TreeNode(2)
t4 = TreeNode(4)
t0.left = t1
t0.right= t2
t1.left = t3
t1.right=t4


ls = []
def Print_Updown(tree):
    if tree == None:
        return 
    ls.append(tree.x)
    def AppendLeftRight(tree):
        if tree == None:
            return
        global ls
        if tree.left != None:
            ls.append(tree.left.x)
        if tree.right != None:
            ls.append(tree.right.x)
        AppendLeftRight(tree.left)
        AppendLeftRight(tree.right)
        return
    AppendLeftRight(tree)
    return 
    
Print_Updown(t0)
print(ls)