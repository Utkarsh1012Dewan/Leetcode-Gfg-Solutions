class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        max_difficulty = max(difficulty)
        max_Upto_Difficulty = [0] * (max_difficulty + 1)

        #mapping each difficulty to its profit
        for d, p in zip(difficulty, profit):
            max_Upto_Difficulty[d] = max(max_Upto_Difficulty[d], p)

        #keeping a track of the maxProfit upto a difficulty
        for i in range(1, max_difficulty + 1):
            max_Upto_Difficulty[i] = max(max_Upto_Difficulty[i], max_Upto_Difficulty[i - 1])

        profit = 0
        for ability in worker:
            if ability > max_difficulty:
                profit += max_Upto_Difficulty[max_difficulty]
            else:
                profit += max_Upto_Difficulty[ability]

        return profit
        