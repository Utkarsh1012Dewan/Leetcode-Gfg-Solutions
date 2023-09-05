class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def dfs(index,temp,target):

            if target == 0:
                res.append(temp[:])
                return
            if target <= 0:
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                
                temp.append(candidates[i])
                dfs(i+1,temp,target-candidates[i])
                temp.pop()
        
        dfs(0,[],target)

        return res