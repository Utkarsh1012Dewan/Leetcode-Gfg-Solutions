class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        ans,left,total = len(nums),0,0
        #1 4 1 7 3 0 2 5
        #10
        #total = 1, 5, 6, 13, 12, 8, 11, 10, 
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans,right-left+1)
                total -= nums[left]
                left+=1

        return ans
            