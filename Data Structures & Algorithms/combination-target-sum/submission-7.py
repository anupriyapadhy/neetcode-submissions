class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output=[]
        def dfs(result,index,remaining):
            if  remaining==0:
                output.append(result.copy())
                return
            if remaining < 0 or index >= len(nums):
                return
            result.append(nums[index])
            dfs(result,index,remaining-nums[index])
            result.pop()
            dfs(result,index+1,remaining)    

        dfs([],0, target)
        return output
        