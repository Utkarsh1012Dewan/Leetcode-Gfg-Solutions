class Solution:
    def validStrings(self, n: int) -> List[str]:

        def backtrack(current,remaining):
            if remaining  == 0:
                result.append(current)
                return
            
            if current == "" or current[-1] == "1":
                backtrack(current + "0", remaining - 1)
            backtrack(current + "1", remaining - 1)
    
        result = []
        backtrack("",n)
        return result