def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n-i-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr  

arr=list(map(int,input().split()))
print(bubble_sort(arr))
