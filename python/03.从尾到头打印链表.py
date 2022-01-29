# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:05:38 2022

@author: fanyong
"""

from nodes import Node

def PrintLinkedLsFromTail2Head(head):
    outs = []
    p = head
    while p != None:
        outs.insert(0,p.x)
        p = p.next
    return outs