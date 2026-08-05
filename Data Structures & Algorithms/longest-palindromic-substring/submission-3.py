class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="": return ""
        def isPal(left:int,right:int)-> int:
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1

        start,end =0,0
        for i in range(len(s)):
            oddlen=isPal(i,i)
            evenlen=isPal(i,i+1)
            maxlen=max(oddlen,evenlen)
            if maxlen>end-start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2

        
        return "".join(s[start:end+1])
            

        