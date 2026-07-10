class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def dfs(index,arr):
            if index==len(nums):
                output.append(arr[:])
                return
            arr.append(nums[index])
            dfs(index+1,arr)
            arr.pop()
            dfs(index+1,arr)
        dfs(0,[])
        return output
        