class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res,maxFreq,left=0,{},0
        for right in range(len(s)):
            maxFreq[s[right]]=maxFreq.get(s[right],0)+1
            while right-left+1 - max(maxFreq.values())>k:
                maxFreq[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
