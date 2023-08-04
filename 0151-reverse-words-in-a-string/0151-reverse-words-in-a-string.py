class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = list(s.strip().split())
        
        i = 0
        j = len(l) - 1
        
        
        while i < j:
            l[i],l[j] = l[j],l[i]
            i+=1
            j-=1
            
        
        return ' '.join(l)
        