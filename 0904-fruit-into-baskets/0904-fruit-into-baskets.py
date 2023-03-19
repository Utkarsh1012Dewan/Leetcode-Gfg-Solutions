class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        #solution 2
        counter, left = defaultdict(int), 0
        for right, fruit in enumerate(fruits):
            counter[fruit] += 1
            if len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    counter.pop(fruits[left])
                left += 1
        return right - left + 1
        
        
        # solution 1
        baskets = 2
        
        start = end = 0
        track = {}
        maxLen = float("-inf")
        
        for end in range(len(fruits)):
            if fruits[end] not in track:
                track[fruits[end]] = 0
            track[fruits[end]] += 1
            
            while len(track) > baskets:
                track[fruits[start]] -=1
                if track[fruits[start]] == 0:
                    del track[fruits[start]]
                start +=1
            
            maxLen = max(maxLen, end-start+1)
            
        
        return maxLen
        
        
        
        
        