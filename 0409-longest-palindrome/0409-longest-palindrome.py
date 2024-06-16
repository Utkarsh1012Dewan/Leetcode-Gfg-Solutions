from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:

        track = set()
        res = 0

        for i in s:
            if i in track:
                #if i in track means we have 2 of those characters
                #that means they can be used to create a palindrome
                #so we remove that from set and append 2 to res
                track.remove(i)
                res +=2
            else:
                track.add(i)
        #even if we have multiple chaarcters here
        #i.e they were unique, only one will be needed to
        #increase the length of the palindrome i.e res+1
        return res + 1 if track else res





#Wrong code
        # if len(s) == 1:
        #     return 1
        # track = defaultdict(int)

        # for i in s:
        #     track[i] +=1
        # isEven,isOdd = 0,0
        # evenTotal,oddTotal = 0,0
        # oddMaxFreq = 0

        # for i in track:
        #     if track[i]  %2 == 0:
        #         isEven +=1
        #         evenTotal += track[i]
        #     else:
        #         isOdd +=1
        #         oddTotal += track[i]
        #         oddMaxFreq = max(oddMaxFreq,track[i])
                    
        # if len(s) % 2 == 0 and isOdd == 0:
        #     return evenTotal
        # elif len(2) % 2 == 0 and isOdd > 0:
        #     evenTotal + oddMaxFreq 

        # elif isOdd % 2 == 0:
        #     return evenTotal + oddMaxFreq
        # else:
        #     return evenTotal + oddTotal
        

        