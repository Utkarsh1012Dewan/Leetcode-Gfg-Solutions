class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r  = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True

  # MY OWN - Time and space = O(N)
#         if s == " ": 
#             return True
        
#         new = ("".join(i for i in s if i.isalnum())).lower()
        
#         l,r = 0 , len(new) - 1
        
#         while l <=r:
#             if new[l] != new[r]:
#                 return False
#             l+=1
#             r-=1
        
#         return True

            
            