class Solution:
#MORE OPTIMIZED APPROACH
    def helper(self,arr):
        max_ele = max(arr)
        min_ele = min(arr)

        #this calculates the remainder when the range of the array (i.e., the difference b/w the max and min elements) is divided by the number of gaps between the elements (which is len(arr) - 1).
        if (max_ele-min_ele) % (len(arr)-1) != 0:
            return False
        diff = (max_ele-min_ele) / (len(arr)-1)

        new = set(arr)
        curr = min_ele + diff
        while curr < max_ele:
            if curr not in new:
                return False
            curr += diff
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            ans.append(self.helper(arr))
        
        return ans

    





#LESS OPTIMIZED APPROACH
        # ans = [False]*len(l)

        # for i in range(len(l)):
        #     subarray = sorted(nums[l[i]:r[i]+1])
        #     diff = subarray[1] - subarray[0]
        #     ans[i] = True
        #     for j in range(1, len(subarray)):
        #         if subarray[j] - subarray[j-1] != diff:
        #             ans[i] = False
        #             break

        # return ans

                





        