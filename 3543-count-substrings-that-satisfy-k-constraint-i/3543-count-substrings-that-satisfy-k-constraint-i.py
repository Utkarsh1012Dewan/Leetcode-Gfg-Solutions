class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        total = 0
        zeroes = ones = 0
        left = 0

        for right in range(len(s)):
            if s[right] == '1':
                ones +=1
            else:
                zeroes += 1
            
            while ones > k and zeroes > k:
                if s[left] == '0':
                    zeroes -=1
                else:
                    ones -=1
                left += 1
            total += right - left + 1
        
        return total

        