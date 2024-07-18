class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        #Without using stack
        opened,closed = 0,0

        for i in s:
            if i == "(":
                opened +=1
            elif i == ")" and opened > 0:
                opened -=1
            else:
                closed +=1
        
        return opened + closed

        # #Using Stack
        # stack = []

        # for i in s:
        #     if stack and i == ")" and stack[-1] == "(":
        #         stack.pop() 
        #     else:
        #         stack.append(i)
        

        # return len(stack)




        