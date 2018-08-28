# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:04:24 2018

@author: Anil Kumar Koundal

My implementation of Selection sort method for sorting list in ascending and descending order.
"""

def sort(arr):
    
    for i in range(len(arr)-1):
        min_ = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[min_]):
                min_ = j
        
        temp = arr[min_]
        arr[min_] = arr[i]
        arr[i] = temp
        
    return arr

def reverse_sort(arr):
    
    for i in range(len(arr)-1):
        max_ = i
        for j in range(i+1,len(arr)):
            if(arr[j] > arr[max_]):
                max_ = j
        
        temp = arr[max_]
        arr[max_] = arr[i]
        arr[i] = temp
        
    return arr

num=[12,2,23,4,5,21,34,8,8]
print(sort(num))
print(reverse_sort(num))