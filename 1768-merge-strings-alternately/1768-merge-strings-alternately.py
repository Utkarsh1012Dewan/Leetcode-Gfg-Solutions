class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i  = 0
        builder = []
        x,y = len(word1),len(word2)
        
        while x and y:
            builder.append(word1[i])
            x-=1
            builder.append(word2[i])
            y-=1
            i+=1
        
        if x:
            builder.append(word1[i:])
                
        if y:
            builder.append(word2[i:])
            
        
        return "".join(builder)