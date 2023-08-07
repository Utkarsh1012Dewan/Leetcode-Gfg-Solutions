class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        track = {}
        
        for i in nums:
            track[i] = 1 + track.get(i,0)
            
        count  = 0
        
        for i in track:
            if track[i] > 1:
                count += (track[i]*(track[i]-1))//2
        
        return count
        