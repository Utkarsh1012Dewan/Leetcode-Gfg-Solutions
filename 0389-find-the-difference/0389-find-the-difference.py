class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            return t
        
        hashTable = {}
        
        for i in t:
            hashTable[i] = 1+hashTable.get(i,0)
        
        
        for i in s:
            if i in hashTable:
                hashTable[i] -=1
                
                if hashTable[i] == 0:
                    del hashTable[i]
        
        for i in hashTable:
            return i