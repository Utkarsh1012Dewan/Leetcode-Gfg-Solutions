class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #optimised
#         track = nums[0]
#         count = 1
        
#         for i in range(1,len(nums)):
#             if nums[i] == track:
#                 count +=1
#             else:
#                 if count == 0:
#                     track = nums[i]
#                     count = 1
                    
#                 else:
#                     count -=1
        
#         return track
        
    
        #brute force
        
        track = {}
        
        for i in nums:
            track[i] = 1 + track.get(i,0)
        
        max = -1
        ans = None
        
        for i in track:
            if track[i] >= max:
                max = track[i]
                ans = i
        
        return ans
        
        
        
        
        
        