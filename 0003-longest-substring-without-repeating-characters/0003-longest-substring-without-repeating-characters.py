class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        indexMap = {}
        maxLen = 0
        
        for end in range(len(s)):
            
            right_char = s[end]
            
            if right_char in indexMap:
                
                start = max(start, indexMap[right_char] + 1)
            
            indexMap[right_char] = end
            
            maxLen = max(maxLen, end-start+1)
            
        
        return maxLen