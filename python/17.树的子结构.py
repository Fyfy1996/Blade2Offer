# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:25:31 2021

@author: fanyong
"""
class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right= None


t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t0.left = t1
t0.right= t2
t1.left = t3
t1.right= t4


s1 = TreeNode(1)
s2 = TreeNode(3)
s3 = TreeNode(4)
s1.left = s2
s1.right= s3




def Print_PreOrder(node):
    if node == None:
        return []
    return Print_PreOrder(node.left) + [node.x] + Print_PreOrder(node.right)

def IsSameTree(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    else:
        return (tree1.x == tree2.x) & IsSameTree(tree1.left, tree2.left) & IsSameTree(tree2.right, tree2.right)

print(IsSameTree(t1, s1))

def IsSubTree(tree, subtree):
    if tree == None:
        return False
    if tree.x == subtree.x:
        return IsSameTree(tree, subtree)
    else:
        left = IsSubTree(tree.left, subtree)
        right = IsSubTree(tree.right, subtree)
        return left | right
    
print(IsSubTree(t0, s1))
