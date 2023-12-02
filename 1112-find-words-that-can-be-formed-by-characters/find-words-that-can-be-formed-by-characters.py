class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_count = collections.Counter(chars)
        #or do the above operation manually

        for word in words:
            word_count = collections.Counter(word)
            for char in word_count:
                if word_count[char] > chars_count[char]:
                    break
            else: # This else clause corresponds to the for loop
                ans += len(word)
    
        return ans
