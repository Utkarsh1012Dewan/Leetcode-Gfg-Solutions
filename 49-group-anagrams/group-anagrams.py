from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)
        
        for i in strs:
            keys = [0]*26
            for j in i:
                
                keys[ord(j)-ord('a')] +=1
            
            hashMap[tuple(keys)].append(i)
            
        
        return hashMap.values()
        