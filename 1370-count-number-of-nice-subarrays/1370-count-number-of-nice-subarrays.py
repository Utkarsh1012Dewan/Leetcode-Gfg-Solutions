class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res,odd = 0,0
        l,m = 0,0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd +=1

            while odd > k:
                if nums[l] % 2:
                    odd-=1
                l+=1
                m = l
            
            if odd == k:
                while not nums[m] % 2:
                    m+=1
                res += (m-l) + 1
        
        return res







# #My attempt
#         count = 0
#         temp = 0
#         l = 0
#         currCount = 0

#         for r in range(len(nums)):
#             if nums[r] % 2 != 0:
#                 temp +=1

#             while temp > k:
#                 if nums[l] % 2 == 0:
#                     currCount = count
#                     count += currCount
#                 else:
#                     temp -=1
#                 l+=1

#             if temp == k:
#                 count +=1
        
#         if l == 0:
#             while temp >= k:
#                 if nums[l] % 2 == 0:
#                     l+=1
#                     currCount = count
#                     count += currCount
#                 else:
#                     temp -=1
#                     l+=1

#         return count


        
# 2,2,2,1,2,2,1 * with every combination of next(2,2,2) =
# [2,2,2,1,2,2,1], [2,2,2,1,2,2,1,2], [2,2,2,1,2,2,1,2,2], [2,2,2,1,2,2,1,2,2,2]

# 2,2,1,2,2,1 * with every combination of next(2,2,2) =
# [2,2,1,2,2,1], [2,2,1,2,2,1,2], [2,2,1,2,2,1,2,2], [2,2,1,2,2,1,2,2,2]

# 2,1,2,2,1 * with every combination of next(2,2,2) =
# [2,1,2,2,1], [2,1,2,2,1,2], [2,1,2,2,1,2,2], [2,1,2,2,1,2,2,2]

# 1,2,2,1 * with every combination of next(2,2,2) =
# [1,2,2,1], [1,2,2,1,2], [1,2,2,1,2,2], [1,2,2,1,2,2,2]