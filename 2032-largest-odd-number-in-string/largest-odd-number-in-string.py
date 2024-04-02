class Solution:
    def largestOddNumber(self, num: str) -> str:

        n = len(num)

        odds = set('13579')
        if num[-1] in odds:
            return num

        for i in range(len(num)-1,-1,-1):
            if num[i] in odds and i < n-1:
                return num[:i+1]
                
        
        return ""
        