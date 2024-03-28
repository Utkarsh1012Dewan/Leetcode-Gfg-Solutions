class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        track = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(nums)):
            track[nums[r]] +=1
            while track[nums[r]] > k:
                track[nums[l]] -=1
                l+=1
            
            ans = max(ans, r-l+1)

        return ans