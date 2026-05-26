class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text1)>len(text2):
            text1,text2=text2,text1
        m,n=len(text1), len(text2)
        prevrow=[0]*(n+1)
        currrow=[0]*(n+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    currrow[j]=prevrow[j-1]+1
                else:
                    currrow[j]=max(prevrow[j],currrow[j-1])
            prevrow=currrow
            currrow=[0]*(n+1)
        return prevrow[-1]
    




        