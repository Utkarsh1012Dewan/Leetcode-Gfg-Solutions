class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # l,r = 0,c

        # while l <= r:
        #     mid = (l+r)//2

        #     if l*l + (mid*mid) == c or r*r + (mid*mid) == c:
        #         return True
        #     elif l*l + (mid*mid) > c:
        #         r = mid -1
        #     else
        #         l = mid + 1
        
        # return False

#l - 0 
#r - 5
#mid - 2
#4



# #Two Pointer -> Gives TLE
        l,r = 0,int(sqrt(c))

        while l <= r:
            if (l*l) + (r*r) == c:
                return True
            elif (l*l) + (r*r) > c:
                r-=1
            elif (l*l) + (r*r) < c:
                l+=1
        
        return False


