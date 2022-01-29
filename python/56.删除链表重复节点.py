# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:56:39 2021

@author: fanyong
"""
class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        
def print_LinkedLs(ls):
    p0 = ls
    while p0 != None:
        print(p0.x)
        p0 = p0.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(3)
n5 = Node(3)
n6 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


def DeleteNode(header):
    if header.next == None:
        return header
    pPrev = None
    pCur = header
    pNext = None
    while pCur != None:
        if (pCur.next != None) and (pCur.x == pCur.next.x):
            pNext = pCur.next
            while (pNext != None) and (pCur.x == pNext.x):
                pNext = pNext.next
            if pPrev == None:
                header = pNext
            else:
                pPrev.next = pNext
            pCur = pNext
        else:
            pPrev = pCur
            pCur = pCur.next
    return header

newhead = DeleteNode(n1)

print_LinkedLs(newhead)
    