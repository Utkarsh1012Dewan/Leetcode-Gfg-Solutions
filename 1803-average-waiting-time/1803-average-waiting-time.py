class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        total = 0
        wait = 0

        for cust in customers:
            #if the current total time passed is greater than the incoming time of the customer
            if total > cust[0]:
                #then the waiting time is
                #since the customer already arrived before the previous order was finished
                #and will have to wait a frew extra minutes for it to be finished
                wait += cust[1] + (total - cust[0])
            else:
                #else the waiting time is simply
                #the time it will take to prepare the order
                wait += cust[1]

            #if the incoming time of the customer is much later than the 
            #prepare time for the previous orders
            #new total time passed will be
            #new incomning time of the customer + the wait time for the order to be prepared
            if cust[0] > total:
                total = cust[0] + cust[1]
            else:
                #else the total time passed will simply increase by
                #the time it takes to prepare the order for the customer
                total += cust[1]

        return wait/len(customers)





        