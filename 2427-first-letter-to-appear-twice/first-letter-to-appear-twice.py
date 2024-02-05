class Solution:
    def repeatedCharacter(self, s: str) -> str:

        track = set()

        for i in s:
            if i in track:
                return i
            else:
                track.add(i)
        
        