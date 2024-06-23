class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxQ,minQ = deque(),deque()
        l = 0
        r = 0
        ans = 0

        while r < len(nums):
            while minQ and nums[r] <= nums[minQ[-1]]:
                minQ.pop()
            while maxQ and nums[r] >= nums[maxQ[-1]]:
                maxQ.pop()
            minQ.append(r)
            maxQ.append(r)

            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                l+=1
                if l > minQ[0]:
                    minQ.popleft()
                if l > maxQ[0]:
                    maxQ.popleft()
            
            ans = max(ans,r-l+1)
            r+=1

        return ans

        