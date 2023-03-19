class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False
        
        valid = { '(' : ')' , '[' : ']' , '{' : '}' }
        stack  = []
        
        for i in s:
            if i in valid:
                stack.append(i)
            elif stack and valid[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        
        