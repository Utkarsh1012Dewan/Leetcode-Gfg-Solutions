class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        end = len(s)-1

        while end > 0 and s[end] == " ":
            end -=1
        beg = end

        while beg >= 0 and s[beg] != " ":
            beg -=1
        
        return end-beg



        # s = s.strip()
        # count = 0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] == " ":
        #         return count
        #     else:
        #         count +=1
        
        # return count

        
        
        #using inbuilt functions
#         new = s.strip().split(' ')
        
#         return len(new[-1])
        
        
        
        
        
        
        
        
        
            
        