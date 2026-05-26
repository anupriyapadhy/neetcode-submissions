class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,n=[],len(nums)
        def dfs(idx,nums):
            if idx==n:
                res.append(nums[:])
                return
            for i in range(idx,n):
                nums[idx],nums[i]=nums[i],nums[idx]
                dfs(idx+1,nums)
                nums[idx],nums[i]=nums[i],nums[idx]

        dfs(0,nums)
        return res

        