class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = {}
        for i in magazine:
            count[i] = 1 + count.get(i,0)

        
        for i in ransomNote:
            if i not in count:
                return False
            elif i in count:
                count[i] -=1
                if count[i] == 0:
                    del count[i]
        
        return True
        





        