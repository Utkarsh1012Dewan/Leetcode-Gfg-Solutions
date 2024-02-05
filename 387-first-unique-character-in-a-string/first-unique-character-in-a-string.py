class Solution:
    def firstUniqChar(self, s: str) -> int:

        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')] +=1
        
        for i in range(len(s)):
            if arr[ord(s[i])-ord('a')] == 1:
                return i
        
        return -1




#better solution

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         arr = [0]*26
#         for i in range(len(s)):
#             arr[ord(s[i]) - ord('a')] += 1
        
#         for i in range(len(s)):
#             if arr[ord(s[i]) - ord('a')] == 1:
#                 return i

#         return -1
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
        
#         track = {}
        
#         for i in s:
#             track[i] = 1+track.get(i,0)
        
#         check = 0
        
#         for i in track:
#             if track[i] == 1:
#                 check =  i
#                 break
#         for i in range(len(s)):
#             if s[i] == check:
#                 return i
        
#         return -1