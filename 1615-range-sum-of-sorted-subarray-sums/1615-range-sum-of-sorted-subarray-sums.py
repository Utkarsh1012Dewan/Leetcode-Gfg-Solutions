class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        ans = []

        for i in range(n):
            total  = 0
            for j in range(i,n):
                total += nums[j]
                ans.append(total)
        ans.sort()
        mod = 10**9 + 7

        return sum(ans[left-1 :right]) % mod

                

        