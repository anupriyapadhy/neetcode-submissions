class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        tot=len(a)+len(b)
        half=(tot)//2
        if len(nums1)>len(nums2):
            a,b=b,a
        l,r=0, len(a)-1
        while True:
            midA=(l+r)//2
            midB=half-midA-2
            Aleft= a[midA] if midA>=0 else float('-inf')
            Aright= a[midA+1] if (midA+1)<len(a) else float('inf')
            Bleft= b[midB] if midB>=0 else float('-inf')
            Bright= b[midB+1] if (midB+1)<len(b) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                if tot%2:
                    return min(Aright,Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1



        
