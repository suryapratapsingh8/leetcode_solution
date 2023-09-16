# cook your dish here
for j in range(int(input())):
    n=int(input())
    l=[0]*n
    for i in range(n//2):
        l[i]=n-(2*i)
        l[-1*(i+1)]=n-(2*i)-1
    if n%2!=0:
        l[n//2]=1
    o=' '.join(str(x) for x in l)
    print(o)