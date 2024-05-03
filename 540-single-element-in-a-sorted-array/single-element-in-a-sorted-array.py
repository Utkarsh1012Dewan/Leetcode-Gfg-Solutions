class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def validChecker(index):
            if index == len(nums)-1:
                return True
            elif index%2:
                return nums[index] != nums[index-1]
            else:
                return nums[index] != nums[index+1]

        l,r = 0,len(nums)-1
        isValid = -1

        while l<=r:
            mid = (l+r)//2
            if validChecker(mid):
                isValid = mid
                r = mid-1
            else:
                l = mid+1

        return nums[isValid]


        
