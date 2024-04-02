class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()

        word = []
        string = []

        for j in range(len(s)-1,-1,-1):
            
            if s[j] == " " and len(word) > 0:
                newWord = "".join(word[::-1])
                string.append(newWord)
                word = []
                continue
            elif s[j] == " " and len(word) == 0:
                continue
            word.append(s[j])
            
        newWord = "".join(word[::-1])
        string.append(newWord)

        return " ".join(string)

