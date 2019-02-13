# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:57:34 2019

@author: Rangita
"""

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,val):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[val,t,[]])
    else:
        root.insert(1,[val,[],[]])
    return root

def insertRight(root,val):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[val,[],t])
    else:
        root.insert(2,[val,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,val):
    root[0]=val

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def buildtree(r):
    



r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())


