class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        count = 0

        for i in s:
            if i == '(':
                stack.append(i)
                count+=1
            elif i == ')' and count > 0:
                stack.append(i)
                count -=1
            elif i != ')':
                stack.append(i)

        filtered = []
        for i in stack[::-1]:
            if i == '(' and count > 0:
                count -=1
            else:
                filtered.append(i)
        
        return "".join(filtered[::-1])





