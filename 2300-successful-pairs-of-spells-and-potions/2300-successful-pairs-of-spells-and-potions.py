class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        pairs = []
        n = len(potions)
        
        for spell in spells:
            index = len(potions) # to find the weakest potion that works(i.e leftmost value/potion whose product will the current spell is >= success). If we get an index that if smaller than this we make the index equal to that value
        
            l,r = 0,n-1
            
            while l<=r:
                mid = (l+r)//2
                
                if spell*potions[mid] >= success:
                    r=mid-1
                    index  = mid #making index = leftmost potion with product >= success
                else:
                    l = mid +1
            
            pairs.append(n-index)
        
        return pairs
            
        