class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        for i,a in enumerate(nums):
            
            #skipping positive numbers because they will never sum to 0
            if a > 0:
                break
            
            #skipping duplicates
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1 
            total = 0
            
            while l < r:
                total = a + nums[l] + nums[r]
                
                if total > 0:
                    r-=1
                elif total < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    
        return res
                