class Solution:
    def findComplement(self, num: int) -> int:

        binary  = bin(num)[2:]

        ans = []

        for i in binary:
            if i == "0": ans.append("1")
            else: ans.append("0")
        

        new = "".join(ans)
        return int(new,2)

        