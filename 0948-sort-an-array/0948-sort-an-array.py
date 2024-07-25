class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        sorted_nums = []
        while nums:
            sorted_nums.append(heapq.heappop(nums))

        return sorted_nums


    
        