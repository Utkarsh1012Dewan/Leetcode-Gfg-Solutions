class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        nums.sort(reverse =True)
        
        prefix = [nums[0]]
        count = 0
        count +=1 if prefix[-1] > 0 else 0
        
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] > 0:
                count +=1
                
        return count
        