for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()[:n]))
    brr = list(map(int,input().split()[:n]))
    ind = []
    count = 0
    for i in range(1,n+1):
        j = arr.index(i)
        ind.append(j)
        print(ind)
        while len(ind)>=2 and ind[i-2]>=ind[i-1]:
            ind[i-1]+=brr[j]
            count+=1
            print(ind)
    print(count)
        
        
    

    
    
