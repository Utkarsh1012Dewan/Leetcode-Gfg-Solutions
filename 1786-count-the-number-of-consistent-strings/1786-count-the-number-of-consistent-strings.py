class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        track = set(list(allowed))
        count = 0

        for word in words:
            flag = True
            for i in word:
                if i not in track:
                    flag = False
                    break
            if flag:
                count +=1
        
        return count
 
        