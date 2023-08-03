import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        #O(1)
        if (low%2 == 0 and high %2!=0) or (low%2 != 0 and high%2 ==0) :
            return (high-low+1)//2
        
        elif low%2 == 0 and high%2 == 0:
            return (high-low+1)//2
            
        
        elif low%2 != 0 and high%2 != 0:
            return math.ceil((high-low+1)/2) 
        
#         O(n) -> TLE
#         count  = 0
#         for i in range(low,high+1):
#             if i%2 != 0:
#                 count +=1
        
#         return count
        