class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        for i in range(len(nums) - 3):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.findPairs(nums,target,i,j,res)
                
        return res
                    
    def findPairs(self,nums,target,first,second,res):
        
        left = second + 1
        right = len(nums) - 1
        total = 0
        
        while left < right:
            total = nums[first]+nums[second]+nums[left]+nums[right]
            
            if total == target:
                res.append([nums[first],nums[second], nums[left], nums[right]])
                left +=1
                right -=1
                
                
                while left < right and nums[left] == nums[left - 1]:
                    left +=1
                while left < right and nums[right] == nums[right + 1]:
                    right -=1
            
            elif total >= target:
                right -=1
            else:
                left +=1
        return res
            
        
        
                    
                
                        
        