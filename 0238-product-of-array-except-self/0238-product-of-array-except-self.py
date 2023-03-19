class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # product of a number except itself = product of numbers on left * product of numbers on right
        # ex.  arr = [1,2,3,4]
        # prefix product = [1,2,6,24]
        # postfix product = [24,24,12,4]
        # => if we take find product of 2 (i.e index i) expect self, it will be prefix[i-1]*postfix[i+1] 
        
        # since i = 1 for 2 => prefix[0]*postfix[2] = 1*12 = 12
        res = [1]*len(nums)
        
        prefix = 1
        
        for i in range(len(nums)):
            res[i] =  prefix
            prefix *= nums[i]
            
        
        postfix = 1
        
        for i in range(len(nums) - 1 ,-1 ,-1):
            res[i] *= postfix
            postfix *= nums[i]
            
        
        return res
        