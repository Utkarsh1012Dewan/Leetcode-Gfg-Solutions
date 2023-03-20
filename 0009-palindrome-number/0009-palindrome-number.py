class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        new = 0
        copy =  x
        
        while copy > 0:
            new = new*10 + copy%10
            copy = copy//10
        
        
        return new == x
    
