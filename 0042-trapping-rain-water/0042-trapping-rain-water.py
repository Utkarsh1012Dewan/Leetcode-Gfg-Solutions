class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)
        leftMax = height[0]
        rightMax = height[length-1]
        
        l,r = 1, length - 2
        ans = 0
        
        while l <= r:
            if leftMax < rightMax:
                if height[l] > leftMax:
                    leftMax = height[l]
                    l+=1
                else:
                    ans += (leftMax - height[l])
                    l+=1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                    r-=1
                else:
                    ans += (rightMax - height[r])
                    r-=1
        return ans