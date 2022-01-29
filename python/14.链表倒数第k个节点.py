# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:58 2022

@author: fanyong
"""


from nodes import Node

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n0.next = n1
n1.next = n2
n2.next = n3


def LastKNodeInLinkedLs(head, k):
    p,p1 = head, head
    outs = None
    cnt = 0
    flag = False
    while p.next != None:
        if cnt == k:
            flag = True
        p = p.next
        if flag:
            p1 = p1.next
        cnt += 1
    # 此时p指向最后一个节点,如果 k == len(链表) 应该把flag设为true
    if cnt == k:
        flag = True
    outs = p1.x if flag else None
    return outs

print(LastKNodeInLinkedLs(n0, 3))
        