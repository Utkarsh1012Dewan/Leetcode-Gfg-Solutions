class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:

        mod = 10**9 + 7
        a = [1 for x in range(n)]

        i = 1
        while k:
            for i in range(1,n):
                a[i] = a[i] + a[i-1]
            k-=1

        return a[-1] % mod    

        