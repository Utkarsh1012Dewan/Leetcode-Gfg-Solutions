class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        total = 0
        zeroes = ones = 0
        l = 0

        for r in range(len(s)):
            if s[r] == '1':
                ones +=1
            else:
                zeroes += 1
            while ones > k and zeroes > k:
                if s[l] == '0':
                    zeroes -=1
                else:
                    ones -=1
                l += 1
            total += r - l + 1
        
        return total

        