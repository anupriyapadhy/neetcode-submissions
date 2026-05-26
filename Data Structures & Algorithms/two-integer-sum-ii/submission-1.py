class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            remainder=target-numbers[left]
            if remainder<numbers[right]:
                right-=1
            elif remainder==numbers[right]:
                 return[left+1,right+1]
            else:
                left+=1
        return []