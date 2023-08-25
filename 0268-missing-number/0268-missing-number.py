class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #bit manipulation s0lution
        
        total = 0
        
        for i,ele in enumerate(nums):
            total ^= (i+1^ele)
            
        return total
        
        
        
        #naive solution
        
#         n = len(nums)
        
#         total = n*(n+1)//2
        
#         for i in nums:
#             total -=i
            
#         return total
        