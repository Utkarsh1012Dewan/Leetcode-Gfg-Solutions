class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = 0
        start = 0
        tempSum = 0
        l=1
        
        for end in range(len(nums)):
            tempSum += nums[end]
            
            if tempSum > goal:
                
                while start < end and tempSum > goal:
                    tempSum -= nums[start]
                    start +=1
                l = 1
            
            if tempSum == goal:
                while start < end and not nums[start]:
                    start +=1
                    l +=1
                count +=l
            
        
        return count
                
                
            