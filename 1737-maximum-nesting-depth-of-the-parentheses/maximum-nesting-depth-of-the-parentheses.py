class Solution:
    def maxDepth(self, s: str) -> int:

        if s == "":
            return 0

        count = 0
        maxCount = 0

        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                count +=1
            elif s[i] == ')':
                maxCount = max(maxCount,count)
                stack.pop()
                count -=1
            else:
                continue
        
        return maxCount 

        