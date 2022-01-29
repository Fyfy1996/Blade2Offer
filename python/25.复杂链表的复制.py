# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:46:22 2022

@author: fanyong
"""
class ComplexNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.subling = None
  
        
def printComplexNode(complexNode):
    """
    展示复杂链表的函数"""
    p = complexNode
    while p:
        print("Node", p.data, "->", p.next.data if p.next else "None", ">>", 
              p.subling.data if p.subling else "None" )
        p = p.next

node1 = ComplexNode(1)
node2 = ComplexNode(2)
node3 = ComplexNode(3)
node4 = ComplexNode(4)
node5 = ComplexNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.subling = node3
node3.subling = node5
node2.subling = node4
node4.subling = node1
node5.subling = node2

printComplexNode(node1)
print("====")

def DuplicateComplexLinkedLs(head):
    p = head
    while p != None:
        newNode = ComplexNode(p.data)
        newNode.next = p.next
        p.next = newNode
        p = newNode.next
    cnt = 1
    p = head
    p1 = new_head = head.next
    # printComplexNode(head)
    while p != None:
        p1.subling = p.subling
        p.next = p1.next
        p1.next = p1.next.next if p1.next != None else None
        p =p.next
        p1 = p1.next
    return new_head

new_head = DuplicateComplexLinkedLs(node1)
printComplexNode(new_head)
        
        