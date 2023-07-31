def xorsum(arr,k):
    a=0
    for i in range(len(arr)):
        
        d=0
        for j in range(i,len(arr)):
            d=d^arr[j]
            if d==k:
                a=a+1
         
    return a
            
        
    


arr=list(map(int,input().split()))
k=int(input())
print(xorsum(arr,k))
