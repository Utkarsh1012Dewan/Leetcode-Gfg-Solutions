class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

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