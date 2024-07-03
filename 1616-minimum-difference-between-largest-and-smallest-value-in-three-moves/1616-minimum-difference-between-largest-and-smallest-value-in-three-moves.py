class Solution:
    def minDifference(self, nums: List[int]) -> int:

        nums.sort()
        if len(nums) <= 4:
            return 0
        res = float("inf")

        for l in range(4):
            r = len(nums)-4+l

            res = min(res,nums[r]-nums[l])
        
        return res

        