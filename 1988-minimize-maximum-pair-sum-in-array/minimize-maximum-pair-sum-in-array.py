class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        l = len(nums)
        nums.sort()
        total = 0

        for i in range(len(nums)):

            total = max(total,nums[i]+nums[l-i-1])
        
        return total



        