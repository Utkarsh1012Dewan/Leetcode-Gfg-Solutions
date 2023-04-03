class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        track = {}
        
        for i in magazine:
            track[i] = 1 + track.get(i,0)
            
        for i in ransomNote:
            if i not in track:
                return False
            track[i] -=1
            if track[i] == 0:
                del track[i]
        
        return True
        