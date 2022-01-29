# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:26:18 2021

@author: fanyong
"""
class TreeNode:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right= None
        self.par = None

t= TreeNode(0)
l0 = TreeNode(1)
r0 = TreeNode(2)
l00 = TreeNode(3)
l01 = TreeNode(4)

r00 = TreeNode(5)
l000 = TreeNode(6)

t.left = l0
l0.par = t
t.right = r0
r0.par = t
l0.left = l00
l00.par = l0
l0.right = l01
l01.par = l0

r0.left = r00
r00.par = r0

l00.left = l000
l000.par = l00

def InOrder(tree):
    if tree == None:
        return []
    left = InOrder(tree.left)
    right = InOrder(tree.right)
    return left + [tree.x] + right

print(InOrder(t))


def GetNext(tree):
    if tree == None:
        return None
    if tree.right != None:
        pRight = tree.right
        while pRight.left != None:
            pRight = pRight.left
        pNext =  pRight
    else:
        pPar = tree.par
        if pPar == None:
            pNext = None
        if tree is pPar.left:
            pNext = pPar
        else:
            while pPar.par != None and (pPar.par.right is pPar):
                pPar = pPar.par
            pNext = pPar.par
    return pNext
                
        
print(l0.x)
print(GetNext(l0).x)