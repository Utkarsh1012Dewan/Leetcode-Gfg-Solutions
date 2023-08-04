class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        track = {}
        s = set()
        
        for i in arr:
            track[i] = 1 + track.get(i,0)
        
        for i in track.values():
            s.add(i)
            
        return len(track) == len(s)
        
        
        