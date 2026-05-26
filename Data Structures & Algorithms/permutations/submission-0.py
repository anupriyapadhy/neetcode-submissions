class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,n=[],len(nums)
        def backTrack(index,sol):
            if index==n:
                res.append(sol[:])
                return
            for i in range(index,len(nums)):
                sol[index],sol[i]=sol[i],sol[index]
                backTrack(index+1,sol)
                sol[index],sol[i]=sol[i],sol[index]
            
        backTrack(0,nums)
        return res
        