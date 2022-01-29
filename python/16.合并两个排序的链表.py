# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:55:45 2022

@author: fanyong
"""
from nodes import Node,PrintLinkedLs


def MeregeSortedLists(ls1, ls2):
    head = Node(None)
    p1,p2 = ls1,ls2
    p = head
    while p1 != None and p2!=None:
        if p1.x < p2.x:
            p.next = p1
            p1 = p1.next
            p = p.next
        else:
            p.next = p2
            p2 = p2.next
            p = p.next
    if p1 == None:
        p.next = p2
    else:
        p.next = p1
    return head.next


n0 = Node(0)
n1 = Node(3)
n2 = Node(6)
n3 = Node(9)

n0.next = n1
n1.next = n2
n2.next = n3

m0 = Node(2)
m1 = Node(4)
m2 = Node(8)

m0.next = m1
m1.next = m2

head = MeregeSortedLists(n0, m0)

print(PrintLinkedLs(head))