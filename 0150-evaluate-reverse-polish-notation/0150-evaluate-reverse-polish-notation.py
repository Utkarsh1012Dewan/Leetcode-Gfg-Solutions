class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #["4","13","5","/","+"]
        #[4 , 2 ]
        
        stack = []          
        ans = 0
        
        for i in tokens:
            if i == '+':
                ans = stack.pop() + stack.pop()
                stack.append(ans)
            elif i == '-':
                a,b = stack.pop(), stack.pop()
                ans = b-a
                stack.append(ans)
            elif i == '*':
                ans = stack.pop() * stack.pop()
                stack.append(ans)
            elif i == '/':
                a,b = stack.pop(), stack.pop()
                ans = int(b/a)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[0]
        
        