# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:14:48 2020

@author: ADHIRAJ MAJUMDAR
"""

def isPossible(arr,n,k,ans):
    curr_pos = 0
    studentRequired=1
    for i in range(n):
        if(curr_pos+arr[i]>ans):
            curr_pos = arr[i]
            studentRequired +=1
            if(studentRequired>k):
                return False
        else:
            curr_pos+=arr[i]
    return True

def booksAllocation(arr,n,k):
    if(n<k):
        return -1
    start=0
    end=0
    result =10**9
    sum_books=0
    for i in range(n):
        sum_books+=arr[i]
    end=sum_books
    while(start<=end):
        mid=(start+end)//2
        if(isPossible(arr,n,k,mid)):
            result = min(result,mid)
            end = mid - 1
        else:
            start = mid + 1
    return result
data = [12, 34, 67, 90]
n = len(data)
k=3
print(booksAllocation(data,n,k))