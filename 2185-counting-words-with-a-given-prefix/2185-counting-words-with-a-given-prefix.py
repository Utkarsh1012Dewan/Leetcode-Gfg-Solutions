class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        length = len(pref)
        
        for i in words:
            if i[0:length] ==  pref:
                count +=1
        
        return count
        