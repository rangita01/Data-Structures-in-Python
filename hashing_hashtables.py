# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:31:27 2019

@author: Rangita
"""

hash_table = [[] for _ in range(10)]

def hashing_func(key):
    return key%len(hash_table)

def insert(hash_table, key, value):
    hashV = hash(key) % len (hash_table)
    key_exists = False 
    bucket = hash_table[hashV]
    for i ,kv in enumerate(bucket):
        print(kv)
        if key == kv:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key,value))
    else:
        bucket.append((key,value))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)

def search(hash_table,key):
    hashV = hash(key)%len(hash_table)
    bucket = hash_table[hashV]
    for i,kv in enumerate(bucket):
#        print(kv)
        k,v=kv
        if key == k:
            return v
    
print (search(hash_table, 10)) # Output: Nepal
print (search(hash_table, 20)) # Output: India
print (search(hash_table, 30)) # Output: None

def delete(hash_table, key, value):
    hashV = hash(key) % len (hash_table)
    key_exists = False 
    bucket = hash_table[hashV]
    for i ,kv in enumerate(bucket):
#        print(kv)
        if key == kv:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
    else:
        print("No such value found"
              )   


