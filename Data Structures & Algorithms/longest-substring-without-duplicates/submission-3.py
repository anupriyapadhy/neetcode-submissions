class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        n=len(s)
        seen=set()
        maxLength=0
        while right<n:
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            maxLength=max(maxLength,right-left+1)
            seen.add(s[right])                
            right+=1
        return maxLength