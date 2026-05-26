class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        left, right=0, 0
        while right <len(s):
            
            if s[right]=='#':
                charlen = int(s[left:right])   
                left=right+1       
                right=left+charlen
                res.append(s[left:right])
                left=right
            else:
                right+=1
        return res
