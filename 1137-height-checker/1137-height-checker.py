class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = [0]*101

        for i in heights:
            res[i] +=1
        
        expected = []
        for i in range(1,101):
            #this c will tell how many times the number is occuring in the list
            c = res[i]
            for _ in range(c):
                expected.append(i)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res +=1
        return res

# #Brute Force 0 O(nlogn)
#         arr = sorted(heights)
#         count = 0

#         for i in range(len(heights)):
#             if heights[i] != arr[i]:
#                 count +=1
        
#         return count
        