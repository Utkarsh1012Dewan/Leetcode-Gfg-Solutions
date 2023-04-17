class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxVal = max(candies)
        res = []
        
        for i in candies:
            if i + extraCandies >= maxVal:
                res.append(True)
            else:
                res.append(False)
        
        return res
        