# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:09:14 2019

@author: whnzb
"""
def bubble(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

def main():
    l=[4,3,9,0,4,22,1,3]
    print(bubble(l))

if __name__=="__main__":
    main()
#从第一个元素开始，两个相邻元素依次比较，第一次排序后最大元素位于最后位置，依次进行
    