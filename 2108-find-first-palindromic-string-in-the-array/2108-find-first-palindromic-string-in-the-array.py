class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        isPali = False
        
        for i in words:
            
            if len(i) == 1:
                return i
            
            l,r = 0,len(i)-1
            
            while l<=r:
                if i[l] != i[r]:
                    break
                l+=1
                r-=1
            
                if l >= r:
                    isPali = True
                    break
            
            if isPali == True:
                return i
        
        return ""
        
                    
        