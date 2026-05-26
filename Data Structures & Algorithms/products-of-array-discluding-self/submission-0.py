class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        leftProd=1
        for i in range(len(nums)):
            output[i]=leftProd
            leftProd*=nums[i]
        rightProd=1
        print(output)
        for i in range(len(nums)-1,-1,-1):            
            output[i]*=rightProd
            rightProd*=nums[i]
        return output