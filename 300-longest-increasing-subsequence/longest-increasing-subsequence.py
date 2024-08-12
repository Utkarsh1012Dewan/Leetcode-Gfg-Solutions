class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(i,prev):
            if i == n:
                return 0
            
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            sequence = 0 + helper(i+1,prev)
            if nums[i] > nums[prev] or prev == -1:
                sequence = max(sequence,1 + helper(i+1,i))
            
            dp[i][prev+1] = sequence
            return dp[i][prev+1]

        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        return helper(0,-1)