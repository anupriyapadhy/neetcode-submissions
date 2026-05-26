class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(idx,sub,total):
            
            if total==target:
                res.append(sub.copy())
                return
            for i in range(idx,len(candidates)):
                if i>idx and  candidates[i]==candidates[i-1]:
                    continue
                if total+candidates[i]>target:
                    break
                
                sub.append(candidates[i])
                dfs(i+1,sub,total+candidates[i])
                sub.pop()
        dfs(0,[],0)
        return res


