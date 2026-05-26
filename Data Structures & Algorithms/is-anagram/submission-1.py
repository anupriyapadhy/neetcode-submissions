class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        numbers=[0]*26
        for c in s:
            numbers[ord(c)-ord('a')]+=1
        for c in t:
            numbers[ord(c)-ord('a')]-=1
        return not any(x > 0 for x in numbers)





        