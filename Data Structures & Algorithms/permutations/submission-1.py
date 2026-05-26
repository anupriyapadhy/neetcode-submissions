class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol,n=[],[],len(nums)
        def backTrack():
            if len(sol)==n:
                res.append(sol[:])
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backTrack()
                    sol.pop()
            
        backTrack()
        return res
        