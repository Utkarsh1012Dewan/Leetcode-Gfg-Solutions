class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        ans  = 0
        
        for i in t:
            ans ^= ord(i)
            
        for i in s:
            ans ^=ord(i)
            
        return chr(ans)