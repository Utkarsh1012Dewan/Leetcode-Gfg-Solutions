class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        ans,left = len(cards)+1,0
        track = {}
        #[3, 4, 2, 3, 4, 7]
        for right in range(len(cards)):
            track[cards[right]] = 1 + track.get(cards[right],0)
            while track[cards[right]] > 1:
                ans = min(ans,right-left+1)
                
                track[cards[left]] -=1
                
                if track[cards[left]] == 0:
                    del track[cards[left]]
                left+=1    
                
        return ans if ans != len(cards)+1 else -1
                    