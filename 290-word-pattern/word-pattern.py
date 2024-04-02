class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False

        track = {}
        trackTwo = {}

        for i in range(len(pattern)):

            if pattern[i] in track and track[pattern[i]] != words[i]:
                return False
            if words[i] in trackTwo and trackTwo[words[i]] != pattern[i]:
                 return False

            track[pattern[i]] = words[i]
            trackTwo[words[i]] = pattern[i]

        return True
            



        