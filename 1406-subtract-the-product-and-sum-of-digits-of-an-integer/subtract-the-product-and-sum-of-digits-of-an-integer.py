class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        prod = 1
        total = 0
        diff = 0

        while n > 0:
            dig = n%10
            prod*= dig
            total += dig

            n //= 10
        
        return prod - total


        