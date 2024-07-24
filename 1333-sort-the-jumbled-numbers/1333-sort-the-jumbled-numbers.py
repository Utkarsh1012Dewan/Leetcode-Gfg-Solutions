class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        ans = []
        for i,n in enumerate(nums):
            carry = 0
            base = 1
            if n == 0:
                carry = mapping[n]
            while n > 0:
                digit = n % 10
                n = n // 10
                carry += base * mapping[digit]
                base *= 10
            
            ans.append((carry,i))
        ans.sort()
        return [nums[p[1]] for p in ans]


        