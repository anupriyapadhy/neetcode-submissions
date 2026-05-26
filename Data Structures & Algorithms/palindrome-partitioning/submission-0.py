class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def isPal(curr):
            left,right=0,len(curr)-1
            while left<=right:
                if curr[left]==curr[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        def backTrack(index,curr):
            if index==len(s):                
                res.append(curr[:])
                return
            for i in range(index,len(s)):
                if isPal(s[index:i+1]):
                    curr.append(s[index:i+1])
                    backTrack(i+1,curr)
                    curr.pop()
            
        backTrack(0,[])
        return res
        