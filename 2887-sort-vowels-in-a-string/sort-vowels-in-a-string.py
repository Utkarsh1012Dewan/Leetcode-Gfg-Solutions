class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = ('aeiouAEIOU')
        vow = []
        string = []

        for i in s:
            if i in vowels:
                vow.append(i)

        vow.sort(reverse=True)

        for i in s:
            if i in vowels:
                string.append(vow.pop())
                continue
            string.append(i)

        return "".join(string)

        