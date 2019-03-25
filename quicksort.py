# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:29:06 2019

@author: whnzb
"""

def quicksort(l):
    if len(l)<2:
        return l
    num=l[0]
    startl=[x for x in l[1:] if x<=num]
    endl=[x for x in l[1:] if x>num]
    return sorted(startl)+[num]+sorted(endl)

def main():
    l=[4,1,9,10,5,8,4]
    quicksort(l)
    print (quicksort(l))
    
if __name__=="__main__":
    main()
