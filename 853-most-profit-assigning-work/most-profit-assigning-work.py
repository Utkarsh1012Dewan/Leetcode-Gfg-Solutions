class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        # Find the maximum difficulty to create an array up to this difficulty
        max_difficulty = max(difficulty)
        max_Upto_Difficulty = [0] * (max_difficulty + 1)

        # Map each difficulty to its highest profit
        for d, p in zip(difficulty, profit):
            max_Upto_Difficulty[d] = max(max_Upto_Difficulty[d], p)

        # Update the array so each difficulty has the maximum profit up to that difficulty
        for i in range(1, max_difficulty + 1):
            max_Upto_Difficulty[i] = max(max_Upto_Difficulty[i], max_Upto_Difficulty[i - 1])

        # Calculate total profit by adding the maximum profit for each worker's ability
        total_profit = 0
        for ability in worker:
            # If worker's ability exceeds the maximum difficulty, add the highest possible profit
            if ability > max_difficulty:
                total_profit += max_Upto_Difficulty[max_difficulty]
            else:
                # Otherwise, add the maximum profit for the worker's ability
                total_profit += max_Upto_Difficulty[ability]

        return total_profit
