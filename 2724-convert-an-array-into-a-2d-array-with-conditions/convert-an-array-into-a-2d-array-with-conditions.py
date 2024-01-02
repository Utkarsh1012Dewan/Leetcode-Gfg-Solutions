from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)
        elements = set(nums)
        
        ans = []

        while len(count) > 0:
            temp = []
            for i in elements:
                if count[i] > 0:
                    temp.append(i)
                    count[i]-=1
                    if count[i] == 0:
                        del count[i]
            ans.append(temp)
        return ans
    

