class Solution:
    def largestOddNumber(self, num: str) -> str:

        if int(num[-1]) % 2 != 0:
            return num

        result = 0

        for i in range(len(num)-1,-1,-1):
            if num[i] == 0:
                continue
            if int(num[i]) % 2 != 0:
                result = num[:i+1]
                break

        return "" if result == 0 else str(result)
        