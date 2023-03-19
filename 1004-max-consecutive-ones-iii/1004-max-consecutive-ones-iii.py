class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        max_one = 0
        max_len = 0
        
        for r in range(len(nums)):
            if nums[r] == 1:
                max_one +=1
            
            if (r-l+1 - max_one) > k:
                if nums[l] == 1:
                    max_one -=1
                l+=1
                
        
            
            max_len = max(max_len, r-l+1)
        
        return max_len
        
        
        
        
        