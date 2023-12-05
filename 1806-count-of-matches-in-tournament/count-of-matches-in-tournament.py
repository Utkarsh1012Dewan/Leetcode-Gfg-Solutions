class Solution:
    def numberOfMatches(self, n: int) -> int:

        teams,matches = n,0
        count  = 0

        while teams > 1:
            if teams%2 == 0:
                matches = teams // 2
                count += matches
                teams = teams//2
                
            else:
                matches = (teams-1) //2
                count += matches
                teams = ((teams-1)//2)+1
        return count


        