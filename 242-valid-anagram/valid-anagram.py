class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        mapS,mapT ={},{}
        
        
        for i in s:
            mapS[i] = 1 + mapS.get(i,0)
            
        
        
        for i in t:
            mapT[i] = 1 + mapT.get(i,0)
        
        
        
        
        for i in mapS:
            if mapS[i] != mapT.get(i,0):
                return False
        
        return True