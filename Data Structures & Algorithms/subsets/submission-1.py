class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def subsets(index,subset):
            if index>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            subsets(index+1,subset)
            subset.pop()
            subsets(index+1,subset)
        subsets(0,[])
        return res
        