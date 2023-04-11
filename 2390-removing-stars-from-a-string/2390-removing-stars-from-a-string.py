class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for i in s:
            if i == '*' and stack:
                stack.pop()
                continue
            stack.append(i)
        
        return "".join(stack)