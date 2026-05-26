class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charLastIndex={}
        for i,c in enumerate(s):
            charLastIndex[c]=i
        print(charLastIndex)
        size,end=0,0
        res=[]
        for i,c in enumerate(s):
            size+=1
            end=max(end, charLastIndex[c])
            if i == end:
                res.append(size)
                size = 0
                
        return res
            


        