from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for word in words:
            count = Counter(word)
            for i in cnt:
                #if i is not in count, it is going to default to 0
                #since counter works like a default dict. Remember the dict.get(key,0)
                cnt[i] = min(cnt[i],count[i])
        
        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        
        return res
            
        
















# #Wrong approach. Even if a string does not have a character the other strings might have that char
# #The count of that char can still become equal to the length of the words array
# #Which is going to fail this logic

#         track = defaultdict(int)

#         for word in words:
#             for i in word:
#                 track[i] +=1
        
#         ans = []

#         for i in track:
#             if track[i] < len(words):
#                 track[i] = 0
#             if track[i] == len(words):
#                 track[i] = 1
#             else:
#                 track[i] = track[i]//len(words)

#         for i in track:
#             if track[i] == 0:
#                 continue
#             for _ in range(track[i]):
#                 ans.append(i)

#         return ans
        