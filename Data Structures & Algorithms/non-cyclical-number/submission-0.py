class Solution:
    def isHappy(self, n: int) -> bool:
        slow,fast=n,self.SUmOfSquare(n)
        while slow!=fast:
            fast=self.SUmOfSquare(self.SUmOfSquare(fast))
            slow=self.SUmOfSquare(slow)
        return True if fast==1 else False
    

    def SUmOfSquare(self,n):
        currVal=0
        while n>0:
            remainder=n%10
            currVal+= remainder**2
            n=n//10
        return currVal
