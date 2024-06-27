class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        #O(1)
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

        
        
        
        
        #O(N)
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