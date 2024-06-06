class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        arr = [0] * (len(nums)-1)
        for i in range(1,len(nums)):
            if nums[i] % 2 ==  nums[i-1] % 2:
                arr[i-1] = 0
            else:
                arr[i-1] = 1
        
        preSum = [1]
        for i in arr:
            preSum.append(preSum[-1] + i)

        ans = []
        for s,e in queries:
            if preSum[e] - preSum[s] == e-s:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans

#[0,4]
#nums = [3,4,1,2,6]
#arr = [1,1,1,0]
#preSum = [1,2,3,4,4]
