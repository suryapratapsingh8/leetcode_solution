def lore(arr,diff,num):
    c=0
    for i in arr:
        sub=abs(num-i)
        if sub<=diff:
            c+=1
    return c   
arr=list(map(int,input().split()))
diff,num=map(int,input().split())
print(lore(arr,diff,num))