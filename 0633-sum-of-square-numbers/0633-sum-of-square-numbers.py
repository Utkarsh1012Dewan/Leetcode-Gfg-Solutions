class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #Binary Search
        l,r = 0,int(sqrt(c)) + 1
        for num in range(r+1):
            l,h = num,r
            while l<=h:
                mid = (l+h)//2
                power = (num**2) + (mid**2)

                if power > c:
                    h = mid-1
                elif power < c:
                    l = mid + 1
                else:
                    return True

        return False 


        # #Two Pointer -> O(sqrt(c))
        # l,r = 0,int(sqrt(c))

        # while l <= r:
        #     if (l*l) + (r*r) == c:
        #         return True
        #     elif (l*l) + (r*r) > c:
        #         r-=1
        #     elif (l*l) + (r*r) < c:
        #         l+=1
        
        # return False


