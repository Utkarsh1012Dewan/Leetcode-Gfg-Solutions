class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #iteration
        n = len(nums)
        output = [[]]

        for i in nums:
            output += [[i] + curr for curr in output]

        return output




        #recursive using bakctracking
        res = []
        n = len(nums)

        def dfs(index,n,temp):

            if index == n:
                res.append(temp[:])
                return

            temp.append(nums[index])
            dfs(index+1,n,temp)

            temp.pop()
            dfs(index+1,n,temp)
        
        
        dfs(0,n,[])

        return res