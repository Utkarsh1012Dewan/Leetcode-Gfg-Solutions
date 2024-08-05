class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        duplicate = {}

        for i in arr:
            if i in duplicate:
                duplicate[i] = 0
            else:
                duplicate[i] = 1

        for i in duplicate.keys():
            if duplicate[i] == 1:
                k-=1
                if k == 0:
                    return i
        
        return ""

        
        return ""
             


        