class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        #This will stay there for both the solutions
        #To handle an important edge  case
        if len(nums) <= 4:
            return 0
        res = float("inf")

        #T.C= O(N) -> Using Heap (Extremely clever  solution)
        #Idea->We are going to use heap to keep track of
        #4 smallest and 4 largest elements in the array
        #take  min of smallest[i]-  largest[i], both of which the arrays will be sorted
        res = float("inf")
        small = sorted(heapq.nsmallest(4,nums))
        large = sorted(heapq.nlargest(4,nums))

        for i in range(4):
            res = min(res,large[i]-small[i])
        
        return res


        #TC - O(NLogN)
        #https://www.youtube.com/watch?v=S6cUjbQuTnE
        nums.sort()

        for l in range(4):
            r = len(nums)-4+l

            res = min(res,nums[r]-nums[l])
        
        return res

        