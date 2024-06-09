class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        l = 2 * (n-1)

        r = k % l

        if r < n:
            return r

        else:
            return l - r
        
        #[0,1,2,3,4,5] 
        