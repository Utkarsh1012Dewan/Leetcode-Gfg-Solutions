class Solution:
    def fib(self, n: int) -> int:
        
        #Iterative
        a,b = 0,1
        
        for i in range(n):
            a,b = b, a+b
        
        return a
        
        
        
        
        
        
        
        
        
        
        #Recursive
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)
        