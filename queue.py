# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:50:38 2019

@author: rangita
"""

class queue:
     def __init__(self):
          self.items=[]

     def enqueue(self,val):
          self.items.append(val)

     def dequeue(self,val):
          if len(self.items)>=1:
               return self.items.pop(0)
          else:
               return -1
     def isEmpty(self):
          if len(self.items)>=1:
               return False
          else:
               return True
     def size(self):
          return len(self.items)

