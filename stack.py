# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:29:07 2019

@author: rangita
"""

class stack:
     def __init__(self):
          self.items = []
     def peek(self):
          if len(self.items)>=1:
               return self.items[len(self.items)-1]
          else:
               return -1
     def push(self, value):
          self.items.append(value)
     def pop(self):
          if len(self.items)>=1:
               return self.items.pop()
          else:
               return -1
     def display(self):
          print(self.items)


s=stack()
print(s.peek())
s.push(5)
s.push(6)
s.push(55)
s.push(655)
s.push(545)
s.push(758)
print(s.peek())
s.pop()
s.pop()
print(s.peek())
s.display()
