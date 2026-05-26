class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0, len(heights)-1
        leftMax, rightMax= heights[0], heights[right]
        maxWater=0
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            maxWater=max(area,maxWater)
            if heights[left]<heights[right]:
                left+=1               
            else:
                right-=1
            
        return maxWater