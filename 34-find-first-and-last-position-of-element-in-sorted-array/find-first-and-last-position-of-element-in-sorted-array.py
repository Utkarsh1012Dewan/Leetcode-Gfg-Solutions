class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        #Perform 2 binary searches to find the first and the last position

        start,end = 0 , len(nums)-1
        first_found,last_found = -1 , -1
        
        #first_position
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                first_found = mid
                end = mid-1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1
        
        
        start,end = 0 , len(nums)-1

        #last_position
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                last_found = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1
        
        
        return [first_found,last_found]





        