class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        for i in range(len(nums)-k+1):
            currMax=nums[i]
            for j in range(i,i+k):
                currMax=max(currMax,nums[j])
            output.append(currMax)
        return output

        