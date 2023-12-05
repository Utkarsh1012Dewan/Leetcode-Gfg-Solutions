class Solution:
    def numberOfMatches(self, n: int) -> int:
    #Slightly neater solution
        m = 0

        while n > 1:
            if n %2 == 0:
                m += n //2
                n //=2
            else:
                m+=(n-1) //2
                n = ((n-1)//2) + 1
        
        return m


    #My own solution
        # teams,matches = n,0
        # count  = 0

        # while teams > 1:
        #     if teams%2 == 0:
        #         matches = teams // 2
        #         count += matches
        #         teams = teams//2
                
        #     else:
        #         matches = (teams-1) //2
        #         count += matches
        #         teams = ((teams-1)//2)+1
        # return count


        