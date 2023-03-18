class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #neetcode solution
        
        index = set()
        start = 0
        maxLen = 0
        
        for end in range(len(s)):
            while s[end] in index:
                index.remove(s[start])
                start +=1
            index.add(s[end])
            
            maxLen = max(maxLen, end - start +1)
            
        return maxLen
        
        
        
        