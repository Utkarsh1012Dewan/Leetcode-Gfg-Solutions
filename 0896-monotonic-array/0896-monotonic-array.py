class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return True
        
        isGreat = False
        isSmall = False
        
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                isGreat = True
            if nums[i] > nums[i+1]:
                isSmall = True
                
        if isGreat and isSmall:
            return False
        
        return True
        