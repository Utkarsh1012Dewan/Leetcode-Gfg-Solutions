class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        temp = 0

        for i in range(len(s)):

            if temp == len(t):
                return 0

            if s[i] == t[temp]:
                temp +=1
        
        return len(t)-temp
        