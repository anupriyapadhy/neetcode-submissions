class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,subsets=[],[]
        def dfs(index,subset,total):
            if total==target:
                res.append(subset.copy())
                return
            if index>=len(nums) or total>target:
                return
            subset.append(nums[index])
            dfs(index,subset, total+nums[index])
            subset.pop()
            dfs(index+1,subset, total)
        dfs(0,[],0)
        return res
        