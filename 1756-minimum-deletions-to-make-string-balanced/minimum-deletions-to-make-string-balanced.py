class Solution:
    def minimumDeletions(self, s: str) -> int:

        stack = []
        ans = 0

        for i in s:
            if stack and i == "a" and stack[-1] == "b":
                ans +=1
                stack.pop()
            else:
                stack.append(i)
        
        return ans