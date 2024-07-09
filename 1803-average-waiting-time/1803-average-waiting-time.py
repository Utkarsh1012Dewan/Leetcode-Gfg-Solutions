class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        total = 0
        wait = 0

        for cust in customers:
            if total > cust[0]:
                wait += cust[1] + total - cust[0]
            else:
                wait += cust[1]

            if cust[0] > total:
                total = cust[0] + cust[1]
            else:
                total += cust[1]

        return wait/len(customers)





        