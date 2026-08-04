class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2=0, 0
        
        for i in nums:           
            newRob=max(r2, r1+i)
            r1=r2
            r2=newRob
        return r2
