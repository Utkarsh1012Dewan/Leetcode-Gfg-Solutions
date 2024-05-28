class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0
        l = 0
        res = 0

        for r in range(len(s)):
            curCost += abs(ord(s[r]) - ord(t[r]))

            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            
            res = max(res,r-l+1)
        
        return res






#Seen solution
        # i = 0
        # cost = 0

        # for j in range(len(s)):
        #     maxCost -= abs(ord(s[j]) - ord(t[j]))

        #     if maxCost < 0:
        #         maxCost += abs(ord(s[i]) - ord(t[i]))
        #         i+=1
        
        # return j-i+1
        