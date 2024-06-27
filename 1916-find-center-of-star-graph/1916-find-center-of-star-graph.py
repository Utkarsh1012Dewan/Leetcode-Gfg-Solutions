class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        track = {}

        for edge in edges:
            for i in edge:
                track[i]  = 1 + track.get(i,0)

        maxVal = 0
        key = 0
        for i in track:
            if track[i] > maxVal:
                maxVal = max(maxVal,track[i])
                key = i

        return key        