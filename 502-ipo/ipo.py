class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #project that we can afford. Top pe max value with the capital we have
        maxProfit = [] 
        minCapital = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            #As long as we can afford the project accoridng to out current capital
            #we will keep them in the maxHeap
            #When we extend available capital, the project at the top
            #will be the project with the highest profit that we can currently afford
            while minCapital and minCapital[0][0] <=w:
                c,p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)
            
            #if maxProfits is empty that means,
            #we cannot afford any project 
            if not maxProfit:
                break

            #at the top of the maxHeap we will have the project 
            #with the highest profit tha we can afford
            #according to the caspital that is currently present
            w += -1 * heapq.heappop(maxProfit)
        
        return w