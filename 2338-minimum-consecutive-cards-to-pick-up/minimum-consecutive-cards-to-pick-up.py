class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = defaultdict(int)
        shortest, left = len(cards)+1, 0
        for right in range(len(cards)):
            window[cards[right]] += 1
            while window[cards[right]] == 2:
                shortest = min(shortest, right-left+1)
                window[cards[left]] -= 1
                left += 1
        return shortest if shortest != len(cards)+1 else -1
                