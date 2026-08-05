class Solution:
    def countSubstrings(self, s: str) -> int:
        if s=="": return 0
        def isPal(s:str, left,right)-> int:
            res=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                res+=1
                left-=1
                right+=1
            return res
        left=0
        output=0
        for right in range(len(s)):
            output+=isPal(s,right,right)
            output+=isPal(s,right,right+1)

        return output
            


        