class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        output=0
        
        for n in nums:
            if n-1 not in seen:
                length=1
                while n+length in seen:
                    length+=1                
                output=max(output,length)
                
        return output
        