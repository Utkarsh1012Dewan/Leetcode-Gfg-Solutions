class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        
        def helper(i,nums,dp):

            if i == 0:
                return nums[i]
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]
            pick = nums[i] + helper(i-2,nums,dp)
            notPick = 0 + helper(i-1,nums,dp)

            dp[i] = max(pick,notPick)
            return dp[i]

        
        dp1 = [-1]*(n+1)
        dp2 = [-1]*(n+1)

        arr1 = nums[1:]
        arr2 = nums[0:n-1]

        ans1 = helper(n-2,arr1,dp1)
        ans2 = helper(n-2,arr2,dp2)

        return max(ans1,ans2)



        