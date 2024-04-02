class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        track = {}
        secondTrack = {}

        for i in range(len(s)):
            if s[i] in track and track[s[i]] != t[i]:
                    return False
            elif t[i] in secondTrack and secondTrack[t[i]] != s[i]:
                return False
            
            track[s[i]] = t[i]
            secondTrack[t[i]] = s[i]
            
        
        return True

        