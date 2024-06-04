class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def helper(n):

            if n <= 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            ones = helper(n-1)
            twos = helper(n-2)

            memo[n] = ones+twos

            return memo[n]
        
        return helper(n)
        