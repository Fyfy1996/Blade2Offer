# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:17:51 2022

@author: fanyong
"""

class Stack:
    def __init__(self, x=None):
        if x != None:
            self.ls = [x]
        else:
            self.ls = []
    
    def append(self, x):
        self.ls.append(x)
        
    def pop(self):
        assert self.ls != [], "pop from empty stack"         
        return self.ls.pop()
    

class Queue:
    def __init__(self):
        self._ls1 = []
        self._ls2 = []
        self.is_empty = True
        
    def add(self, x):
        self._ls1.append(x)

        
    def _exchange(self, ls0, ls1):
        while ls0 != []:
            ls1.append(ls0.pop())
        
    def pop(self):
        assert self._ls1 != [], "pop from empty Queue"  
        self._exchange(self._ls1, self._ls2)
        re = self._ls2.pop()
        self._exchange(self._ls2, self._ls1)
        return re
    
    def __len__(self):
        return len(self._ls1)
    
    
#%% Test

queue = Queue()
ls = list(range(10))
for i in ls:
    queue.add(i)

while len(queue) > 0:
    print(queue.pop())