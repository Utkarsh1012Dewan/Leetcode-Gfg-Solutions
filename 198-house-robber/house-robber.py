class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def helper(n):

            if n == 0:
                return nums[n]
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            pick = helper(n-2) + nums[n]
            notPick = helper(n-1) + 0 

            dp[n] = max(pick,notPick)
            return dp[n]

        return helper(n-1)



        