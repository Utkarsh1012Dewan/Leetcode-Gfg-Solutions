class Solution:

    def helper(self,i,target,nums,dp):
        if target == 0:
            return True
        if i == 0:
            return nums[0] == target

        if dp[i][target] != -1:
            return dp[i][target]
        
        notPick = self.helper(i-1,target,nums,dp)
        pick = False
        if target >= nums[i]:
            pick = self.helper(i-1,target-nums[i],nums,dp)
        
        dp[i][target] = pick or notPick
        return dp[i][target]


    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        k = total//2
        dp = [[-1 for i in range(k+1)] for j in range(n)]
        return self.helper(n-1,k,nums,dp)