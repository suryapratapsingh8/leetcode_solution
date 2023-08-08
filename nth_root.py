import math
n,m=map(int,input().split())
l=1
h=m
while h>l:
    mid=(l+h)//2
    if math.pow(mid,n)==m:
        print(mid)
        break 
    elif math.pow(mid,n)>m:
        h=mid 
    else:
        l=mid+1
else:
 print(-1)
