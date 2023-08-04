class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set('aeiouAEIOU')
        l = list(s)
        i,j = 0,len(s)-1

        while i < j:
            while l[i] not in vowels and i<j:
                i+=1
            while l[j] not in vowels and i<j:
                j-=1
            l[i],l[j] = l[j],l[i]
            
            i+=1
            j-=1
        
        return "".join(l)
        
        
        # ->My approach(Wrong)
#         newStr = [0]*len(s)
#         vowels = set('aeiou')
        
#         for i in range(len(s)):
#             if s[i] not in vowels:
#                 newStr[i] = s[i]
#             else:
#                 continue
        
        
#         for i in range(len(s)-1,-1,-1):
#             if s[i] in vowels and newStr[i] == 0:
#                 newStr[i] = s[i]
        
#         return ''.join(newStr)
        
        
        