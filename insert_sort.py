def insert_sort(l):
    for i in range(0,len(l)):
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1]=l[j-1],l[j]
    return l

def main():
    l=[4,3,9,0,3,21,0]
    print(insert_sort(l))
    
if __name__=="__main__":
    main()
    #从第二个数开始，依次插入前面已排好序列中
    