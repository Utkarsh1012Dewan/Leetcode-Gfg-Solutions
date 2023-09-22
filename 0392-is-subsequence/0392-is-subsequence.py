class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        i,j = 0,0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return i == len(s)









        #my solution
        if len(s) == 0:
            return True

        tracker = list(s)

        for i in range(len(t)-1,-1,-1):

            if t[i] == tracker[-1] and tracker:
                tracker.pop()

                if len(tracker) == 0:
                    return True


        return len(tracker) == 0       