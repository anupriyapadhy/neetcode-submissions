class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numbers=defaultdict(list)

        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            numbers[tuple(count)].append(s)

        return list(numbers.values())
            
