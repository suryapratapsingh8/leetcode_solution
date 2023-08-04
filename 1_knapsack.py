class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
  def knapSack(self,W, wt, val, n):
       
        # code here
        dp={}
        def solve(n,capacity):
            if n==0 or capacity==0:
                return 0
            elif (n,capacity) in dp:
                return dp[(n,capacity)]
            else:
                cwt=wt[n-1]
                cval=val[n-1]
                if capacity>=cwt:
                    a=cval+solve(n-1,capacity-cwt)
                    b=solve(n-1,capacity)
                    c= max(a,b)
                    
                else:
                    c= solve(n-1,capacity)
                dp[(n,capacity)]=c
                return c
        return solve(n,W)
    
if __name__=='__main__':
    val=list(map(int,input().split()))
    wt=list(map(int,input().split()))
    W=int(input())
    n=int(input())
    ob=Solution()
    print(ob.knapSack(W,wt,val,n))
    

                    