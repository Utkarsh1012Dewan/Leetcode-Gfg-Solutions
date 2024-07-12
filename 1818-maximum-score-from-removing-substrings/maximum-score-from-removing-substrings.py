class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def solver(s,first,second,score):
            stack = []
            points = 0

            for i in s:
                if stack and stack[-1] == first and i == second:
                    points += score
                    stack.pop()
                else:
                    stack.append(i)
            
            return "".join(stack),points
        
        if x > y:
            s,s1 = solver(s,'a','b',x)
            s,s2 = solver(s,'b','a',y)
        if y > x:
            s,s1 = solver(s,'b','a',y)
            s,s2 = solver(s,'a','b',x)
        
        return s1+s2
