class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        #brute force -> sort and pick the number at the beginneing after
        #checking that it's positive exists in the end of the array

        #Optimized
        track = {}

        for i in nums:
            if i > 0:
                track[i] = 0

        largestNum = -1001

        for i in nums:
            if i < 0 and abs(i) in track:
                if abs(i) > largestNum:
                    largestNum = max(largestNum,abs(i))
        
        return -1 if largestNum == -1001 else largestNum





        