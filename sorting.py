# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:34:59 2019

@author: rangita
"""
#insertion sort
arr = [12, 11, 13, 5, 6]
for i in range(len(arr)):
     key = arr[i]
     j = i-1
     print("key {} j {}".format(key,j))
     while j>=0 and key<arr[j]:
          arr[j+1]=arr[j]
          j-=1
          print("arr in while {}".format(arr))
     arr[j+1]=key
     print("finally arr {}".format(arr))
print(arr)

#bubble sort
a = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(a)):
     for j in range(0,len(a)-i-1):
          if a[j]>a[j+1]:
               a[j],a[j+1]=a[j+1],a[j]
print(a)

#selection sort
b = [64, 25, 12, 22, 11]
for i in range(len(b)):
     minx=i
     for j in range(i+1,len(b)):
          if b[minx]>b[j]:
               minx=j
     b[minx],b[i]=b[i],b[minx]
print(b)

#merge sort
def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

#quick sort
























