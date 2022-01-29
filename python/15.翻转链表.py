# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:48:14 2022

@author: fanyong
"""


from nodes import Node, PrintLinkedLs

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n0.next = n1
n1.next = n2
n2.next = n3


def ReverseLinkedLs(head):
    if head.next == None:
        return head
    prev, curr = head, head.next
    head.next = None
    while curr.next != None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    curr.next = prev
    return curr

print("Original Linked list: ", PrintLinkedLs(n0))
new_head = ReverseLinkedLs(n0)
print("Reversed Linked List: ", PrintLinkedLs(new_head))