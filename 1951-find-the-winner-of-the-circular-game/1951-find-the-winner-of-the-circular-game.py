class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        #More  optimised solution




        #My Solution
        q = deque(i+1 for i in range(n))
        temp = 0
        startedSeen = False

        while len(q) > 1:
            temp = 1
            while temp < k:
                    q.append(q.popleft())
                    temp += 1        
            q.popleft()
    
        return q[0]


        