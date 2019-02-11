# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:23:19 2019

@author: rangita
"""

class deque():
     def __init__(self):
          self.items=[]

     def addFront(self,item):
          self.items.insert(0,item)
     def addRear(self,item):
          self.items.append(item)
     def removeFront(self):
          if len(self.items)>=1:
               return self.items.pop(0)
          else:
               return -1
     def removeRear(self):
          if len(self.items)>=1:
               return self.items.pop()
          else:
               return -1
     def isEmpty(self):
          if len(self.items)>=1:
               return False
          else:
               return True
     def size(self):
          return len(self.items)