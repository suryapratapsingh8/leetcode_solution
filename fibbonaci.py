def fib(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n]= fib(n-1,dp)+fib(n-2,dp)
        return dp[n]

if __name__ == '__main__' :
    t=int(input())
    for i in range (t):
        n=int(input())
        dp=[-1]*(n+1)
        print(fib(n,dp))

