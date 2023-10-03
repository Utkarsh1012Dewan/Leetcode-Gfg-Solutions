class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        track = {}

        for i in nums:
            track[i] = 1 + track.get(i,0)
        
        total = 0

        for i in track.keys():

            t = track[i]

            if t > 1:
                total += (t*(t-1))//2

        return total 
            





        