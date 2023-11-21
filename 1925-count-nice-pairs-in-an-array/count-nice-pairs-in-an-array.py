class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result = 0
        counter = {}

        for num in nums:
            reversed_num = int(str(num)[::-1])

            difference = num - reversed_num

            if difference in counter:
                result += counter[difference]

            counter[difference] = counter.get(difference, 0) + 1

        return result % (10**9 + 7)







        # count  = 0
        # track = {}
        # counts = {}

        # for i in range(len(nums)):
        #     ele = int(str(nums[i])[::-1])
        #     if ele not in track:
        #         track[ele] = i

        # for i in nums:
        #     for j in track:
        #         if int(str(i)[::-1]) == j:
        #             continue
        #         if i+j not in counts:
        #             counts[i+j] = 1
        #         else:
        #             counts[i+j] +=1
        
        # for ele in counts:
        #     if counts[ele] > 1:
        #         count +=1

        # return count 










        