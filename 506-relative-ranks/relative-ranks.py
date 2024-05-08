class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        medal = ["Gold Medal","Silver Medal","Bronze Medal"]
        res = [""]*n
        track = {}

        for i in range(n):
            track[score[i]] = i

        score.sort(reverse=True)

        for i in range(n):
            if i < 3:
                res[track[score[i]]] = medal[i]
            else:
                res[track[score[i]]] = str(i+1)
        
        return res