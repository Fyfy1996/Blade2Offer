# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:40:04 2021

@author: fanyong
"""
from node import TreeNode, Print_PreOrder

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

def RebuildTree(PreOrder, InOrder):
    if PreOrder == []:
        return None
    if len(PreOrder) == 1:
        return TreeNode(PreOrder[0])
    x = PreOrder[0]
    tmp_node = TreeNode(x)
    idx = InOrder.index(x)
    tmp_node.left = RebuildTree(PreOrder[1:idx+1], InOrder[:idx])
    tmp_node.right= RebuildTree(PreOrder[idx+1:], InOrder[idx+1:])
    return tmp_node

pre = [0,1,3,4,2]
ind = [3,1,4,0,2]
print(Print_PreOrder(RebuildTree(pre,ind)))
    