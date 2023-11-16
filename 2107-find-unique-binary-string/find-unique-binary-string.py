class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        l = len(nums[0])
        res = []
        self.backtrack([],res,l) 
        
        for i in res:
            if i not in nums:
                return i

    def backtrack(self,temp,res,n):
        if len(temp) == n:
            res.append(''.join(temp))
            return
        for digit in ['0', '1']:
            temp.append(digit)
            self.backtrack(temp,res,n)
            temp.pop()

        



        




        