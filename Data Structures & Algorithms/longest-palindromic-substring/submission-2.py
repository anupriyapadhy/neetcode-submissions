class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(subString):
            left,right=0, len(subString)-1
            while left<=right:
                if subString[left]!=subString[right]:
                    return False
                left+=1
                right-=1

            return True
        maxLen, output=0,""
        for l in range(len(s)):
            for r in range(l,len(s)):
                if r+1-l>maxLen and isPal(s[l:r+1]):
                    maxLen=r+1-l
                    output=s[l:r+1]
        
        return output
            

        