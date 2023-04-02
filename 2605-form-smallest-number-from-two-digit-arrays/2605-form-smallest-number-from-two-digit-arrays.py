class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        track = {}
        minNum = 10
        
        for i in nums1:
            track[i] = 0
        
        for i in nums2:
            if i in track:
                track[i] +=1
        
        for i in track:
            if track[i] >=1:
                minNum = min(minNum,i)
                
        if minNum < 10:
            return minNum
        
        a,b = min(nums1),min(nums2)
        if a > b:
            a,b = b,a
        
        return a*10 + b
        
        
         
        
        