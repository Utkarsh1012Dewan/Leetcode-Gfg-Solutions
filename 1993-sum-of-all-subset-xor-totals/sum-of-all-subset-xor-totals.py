class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i,temp):
            if i== len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[i])
            dfs(i+1,temp)

            temp.pop()
            dfs(i+1,temp)

        res = []
        dfs(0,[])

        ans = []

        for subset in res:
            xor = 0
            for j in subset:
                xor ^= j
            
            ans.append(xor)
        
        return sum(ans)
        