class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        track = {}
        count  = 0
        
        
        for i in jewels:
            track[i] = 1+track.get(i,0)
            
        
        for i in stones:
            if i in track:
                count +=1
                
        
        return count
        