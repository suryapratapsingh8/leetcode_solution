def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if arr[m]>arr[j]:
                m=j
        arr[i],arr[m]=arr[m],arr[i]
    return arr  
arr=list(map(int,input().split()))
print(selection_sort(arr))