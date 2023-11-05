class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:      

        minEle = -1
        count  = -1
        track = {}

        for i in nums:
            track[i] = 1 + track.get(i,0)

        for i in track:
            if i % 2 == 0:
                if count == -1 and minEle == -1:
                    minEle = i
                    count = track[i]
                elif (track[i] > count) or track[i] == count and i < minEle:
                    minEle = i
                    count = track[i]
        
        return minEle
