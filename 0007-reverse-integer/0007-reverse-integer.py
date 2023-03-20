class Solution:
    def reverse(self, x: int) -> int:
        
        temp = 0
        
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        
        
        
        while x:
            temp = (temp*10) + x%10
            
            x //= 10
            
        return 0 if temp > pow(2,31) else temp*symbol