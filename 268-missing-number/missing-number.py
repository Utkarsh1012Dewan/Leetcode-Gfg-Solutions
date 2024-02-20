class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #bit manipulation s0lution
        
        total = 0
        #using i+1 because we want to cover all the numbers till n. And also missing 0 in the first iteration does not matter because similar number will give us a zero anyways after getting XORed
        for i,ele in enumerate(nums):
            total ^= (i+1^ele)
            
        return total
        
        
        
        #naive solution
        
#         n = len(nums)
        
#         total = n*(n+1)//2
        
#         for i in nums:
#             total -=i
            
#         return total
        