class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        n = len(position)
        position.sort()

        def count(dist):
            #ans = 1 because we have atleast one ball placed at the front
            ans,curr = 1,position[0]
            for i in range(1,n):
                #if the distance between the first ball -> at position[0]
                #is >= d, that means we can try and put a ball there
                #we keep doing this to find how many balls we can place at any given distance
                if position[i] - curr >= dist:
                    ans +=1
                    curr = position[i]
            return ans

        l,r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r-l) // 2

            #if the number of balls placed in at "mid" distance from each other is higher than m
            #then we can increase the distance we can put between the balls
            #necause we need to put all the balls 
            if count(mid) >= m:
                l = mid
            #if the count of balls if lower than m
            #that means the distance between balls is too high and
            #we need to decrease that distance beteween the balls
            else:
                r = mid - 1
        
        return l
        