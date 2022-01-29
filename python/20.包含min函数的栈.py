# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:34:58 2022

@author: fanyong
"""

class StackWithMin:
    def __init__(self):
        self.ls = []
        self.min_flag = False
        
    def append(self, x):
        self.ls.append(x)
        if not self.min_flag:
            self.min_num = x
            self.min_flag= True
        if self.min_num > x:
            self.min_num = x
            
    def pop(self):
        result = self.ls.pop()
        if len(self.ls) == 0:
            self.min_flag = False
            del self.min_num
        return result
    
    def getMin(self):
        assert self.min_flag, "No num in stack"
        return self.min_num
    
    def __len__(self):
        return len(self.ls)
    
    
stack = StackWithMin()
ls = list(range(1,10))
for i in ls:
    stack.append(i)
    
print("min number:", stack.getMin())

while len(stack) >0:
    print(stack.pop())