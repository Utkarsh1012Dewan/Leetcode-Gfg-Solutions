class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        new = s.strip().split(' ')
        
        return len(new[-1])
        
        
        
        
        
        
        
        
        
#         count  = 0
        
#         for in range(len(s)-1,-1,-1):
            
        