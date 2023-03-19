class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = [] # we will append value:index pair (t : i) 
            
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                val,idx = stack.pop()
                res[idx] = i - idx
            stack.append((t,i))
        
        
        return res