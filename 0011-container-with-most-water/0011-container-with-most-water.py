class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        res = area = 0
        
        while l < r:
            area = min(height[l],height[r]) * (r-l)
            res = max(res,area)
            
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r -=1
            
            # Condition where both height[l] and height[r] are equal
            # the elif and else condition canbe condesed into one since both are doing the same thing
            else:
                r-=1
                
        return res
        
        
        
        