class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def combSum(index,curr,total):
            if index>=len(nums) or total>target:
                return
            if total==target:
                res.append(curr.copy())
                return
            
            
            curr.append(nums[index])
            combSum(index,curr,total+nums[index])
            curr.pop()
            combSum(index+1,curr,total)
        combSum(0,[],0)
        return res
        