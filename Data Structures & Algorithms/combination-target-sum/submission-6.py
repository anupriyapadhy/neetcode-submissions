class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output=[]
        def dfs(index,arr):
            
            if sum(arr)==target and index<len(nums):
                output.append(arr[:])
                return
            if index==len(nums) or sum(arr)>target:
                return
            arr.append(nums[index])
            dfs(index,arr)
            arr.pop()
            dfs(index+1,arr)
        dfs(0,[])
        return output