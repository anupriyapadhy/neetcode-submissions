class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        
        def backtrack(index, remaining, path):
            if remaining == 0:
                output.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                # Skip duplicates at the same tree level
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                # Since it's sorted, we can prune if the current number is too large
                if candidates[i] > remaining:
                    break
                    
                path.append(candidates[i])
                # Move to the next index because each element can be used once
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return output