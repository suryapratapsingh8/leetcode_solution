s='mnbvcxzasdfghjklpoiuytrewq'
k=list(s)
v='aeiouAEIOU'
l=0
m=len(k)-1
while l<m:
    if k[l] in v:
        l+=1
    if k[m] not in v:
        m-=1
    
    c=k[l]
    k[l]=k[m]
    k[m]=c
    
print(k)