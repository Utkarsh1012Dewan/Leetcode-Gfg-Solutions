class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    #optmized (O(N))
        largest = 0
        secLargest = 0

        for i in nums:
            if i >= largest:
                secLargest = largest
                largest = i
            elif secLargest < i < largest:
                secLargest = i

        return (largest-1)*(secLargest-1)



    #brute Force (nlogn)
        # nums.sort()

        # return (nums[-1]-1)*(nums[-2]-1)
        