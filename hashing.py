# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:50:48 2019

@author: rangita
"""

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

d = {}

from collections import Counter
d=Counter(arr1)

#for i in arr1:
#     d[i]=arr1.count(i)


for i in arr2:
     if i in d.keys():
          arr2.remove(i)
if arr2:
     print (True)
else:
     print(False)

a = [10 , 15 , 4 , 20]
b = [8 , 4 , 2 , 10]

di = Counter(a+b)

u,n=[],[]
for i in di.keys():
     if di[i]==2:
          n.append(i)
     u.append(i)

print("union {}, intersection {}".format(u,n))


def merger (alist):
     if len(alist)>1:
          mid = len(alist)//2
          left = alist[:mid]
          right = alist[mid:]

          merger(left)
          merger(right)

          i=j=k=0

          while i<len(left) and j<len(right):
               if left[i]<right[j]:
                    alist[k]=left[i]
                    i+=1
                    k+=1
               else:
                    alist[k]=right[j]
                    j+=1
                    k+=1
          while i<len(left):
               alist[k]=left[i]
               i+=1
               k+=1
          while j<len(right):
               alist[k]=right[j]
               j+=1
               k+=1
#Given an array A[] and a number x, check for pair in A[] with sum as x
A = [-8, 1, 4, 6, 10, 45]
merger(A)
sumd = 100

for i in range(len(A)):
     for j in range(i+1,len(A)-1):
          if A[i]+A[j]==sumd:
               print (True)
               break
A = [-8, 1, 4, 6, 10, 45]
d = []
n = 16
for i in range(len(A)):
     if n-A[i]>0 and n-A[i] in d:
          print(True)
     d.append(A[i])

#Minimum delete operations to make all elements of array same
arr= [4, 3, 4, 4, 2, 4]
d= Counter(arr)
e=Counter(arr)
maxd=list(d.keys())[0]
count=0
for i in e.keys():
     print(d[i])
     if d[i]>maxd:
          print("maxd")
          maxd=d[i]
     elif d[i]<maxd and d[i]!=maxd:
          print("lesss")
          count+=d[i]
          del d[i]
     print(count)
     print(d)












