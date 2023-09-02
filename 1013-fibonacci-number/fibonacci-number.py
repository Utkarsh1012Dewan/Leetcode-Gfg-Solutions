class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        if n <= 2:
            return 1
        first = self.fib(n-1)
        last = self.fib(n-2)

        return first+last
        