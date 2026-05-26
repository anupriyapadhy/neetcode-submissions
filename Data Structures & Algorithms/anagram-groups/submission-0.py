class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numbers=defaultdict(list)

        for s in strs:
            numbers[''.join(sorted(s))].append(s)

        return list(numbers.values())
            
