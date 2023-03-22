class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        
        def recur(i,n):
            if i > n//2:
                return s 
            s[i], s[n-i] = s[n-i],s[i]
            recur(i+1,n)
        
        recur(0,n)
    
        
        
        
        
        
        """
        Do not return anything, modify s in-place instead.
        """
        