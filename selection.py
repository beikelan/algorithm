# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:17:54 2019

@author: whnzb
"""
def selection(l):
    for i in range(0,len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[i]:
                min=j
                l[i],l[min]=l[min],l[i]
    return l

def main():
    l=[4,3,9,0,4,22,1,3]
    print(selection(l))
   
if __name__=="__main__":
    main()
#1.在未排序中找到最小元素，放在起始位
#2.在剩余未排序列中再寻找最小元素，放在已排序列末尾
#3.重复以上步骤
    