class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [False]*len(l)

        for i in range(len(l)):
            subarray = sorted(nums[l[i]:r[i]+1])
            diff = subarray[1] - subarray[0]
            ans[i] = True
            for j in range(1, len(subarray)):
                if subarray[j] - subarray[j-1] != diff:
                    ans[i] = False
                    break

        return ans

                





        