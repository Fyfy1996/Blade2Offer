# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:48:35 2022

@author: fanyong
"""

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

# 使用中序遍历 左根右

from nodes import TreeNode, Print_PreOrder

root = TreeNode(10)
l1 = TreeNode(6)
r1 = TreeNode(14)
ll2 = TreeNode(4)
lr2 = TreeNode(8)
rl2 = TreeNode(12)
rr2 = TreeNode(16)
root.left = l1
root.right= r1
l1.left = ll2
l1.right = lr2
r1.left = rl2
r1.right = rr2

Print_PreOrder(root)

def BST2LinkedLs(root):
    if root.left == None and root.right == None:
        return root
    left_re = BST2LinkedLs(root.left)
    right_re = BST2LinkedLs(root.right)
    
    # `left` 为 `.prev`
    # `.right` 为 `.next`
    # 找到左边部分最右节点
    p = left_re
    while p.right != None:
        p = p.right
    p.right = root
    root.left = p
    
    #找到右边部分最左节点
    q = right_re
    while q.left != None:
        q = q.left
    q.left = root
    root.right = q
    return left_re

ls = BST2LinkedLs(root)
p = ls

print("正向：")
while p.right != None:
    print(p.x)
    p = p.right
print(p.x)
    
print("反向：")  
while p != None:
    print(p.x)
    p = p.left