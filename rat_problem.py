def suff_food(r,unit,arr,n):
    k=r*unit 
    f=0
    if n==0:
        return -1
    else:
        for i in range (n):
            f=f+arr[i]
            if f>=k:
                return i+1 
        else: 
            return 0

r=int(input())    
unit=int(input())  
arr=list(map(int,input().split()))
n=len(arr)
print(suff_food(r,unit,arr,n))

     
