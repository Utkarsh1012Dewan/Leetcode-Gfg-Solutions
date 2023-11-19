class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        ans = val = 0

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                val +=1
            ans+=val
        
        return ans






        