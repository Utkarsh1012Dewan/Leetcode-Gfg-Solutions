class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1,max(piles)
        minK = r

        while l <= r:
            mid = (l+r)//2
            ans = self.isEnough(mid,piles)
            if ans <= h:
                minK = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minK

    def isEnough(self,mid,piles):

        ans = 0
        for i in piles:
            ans += math.ceil(i/mid)
        return ans

        
        