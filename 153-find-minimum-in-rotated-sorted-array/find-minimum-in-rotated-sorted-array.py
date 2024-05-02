class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums)-1
        track = 0
        
        for i in range(len(nums)):
            
            mid = (l+r)//2
            if nums[mid] <= nums[-1]:
                track = mid
                r -=1    
            else:
                l+=1
        
        return nums[track]
        
        