class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        tracker = list(s)

        for i in range(len(t)-1,-1,-1):

            if t[i] == tracker[-1] and tracker:
                tracker.pop()

                if len(tracker) == 0:
                    return True


        return len(tracker) == 0       