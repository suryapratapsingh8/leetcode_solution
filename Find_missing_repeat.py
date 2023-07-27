def mandr(arr):
    k=len(arr)
    arr.sort()
    miss=0
    r=0
    for i in range(1,k):
        if arr[i]-arr[i-1]!=1 and arr[i]!=arr[i-1]:
            miss=arr[i-1]+1
        if  arr[i]==arr[i-1]:
            r=arr[i]
    return miss ,r

arr=list(map(int,input().split()))
print(mandr(arr))
            
