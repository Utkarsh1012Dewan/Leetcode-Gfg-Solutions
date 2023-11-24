class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        total = 0

        if len(piles) == 3:
            return piles[1]
        
        i = 1
        while i < len(piles) - (len(piles) / 3):

            total += piles[i]
            i+=2
        
        return total

        