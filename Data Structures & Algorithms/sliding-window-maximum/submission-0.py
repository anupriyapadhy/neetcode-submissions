class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0:return []
        maxElement=nums[0]
        res=[]
        for i in range(k):
            maxElement=max(maxElement,nums[i])
        res.append(maxElement)
        for i in range(k,len(nums)):
            res.append(max(nums[i+1-k:i+1]))
        return res
