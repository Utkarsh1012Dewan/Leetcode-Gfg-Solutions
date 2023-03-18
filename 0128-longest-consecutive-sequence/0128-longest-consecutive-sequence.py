class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #brute force method - sort karke karlo check -> O(nlogn)
        
        
        nums = set(nums)
        best = 0
        
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y +=1
                best = max(best,y-x)
        return best