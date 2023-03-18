from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        for s in strs:
            
            key = [0]*26
            
            for i in s:
                key[ord(i) - ord('a')] +=1
                
            d[tuple(key)].append(s)
            
        
        return d.values()
        
        
        
        
        
        
        
        
        
        
        
        
        