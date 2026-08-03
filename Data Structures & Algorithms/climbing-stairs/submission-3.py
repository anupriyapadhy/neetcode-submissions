class Solution:
    def climbStairs(self, n: int) -> int:
        totalsteps=0
        a,b,c=1,1,0
        if n<=1:
            return 1
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return c


        