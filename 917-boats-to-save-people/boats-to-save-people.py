class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        count = 0
        l,r = 0,len(people)-1
        people.sort()

        while l <= r:
            if people[r] == limit:
                r-=1
                count +=1
            elif people[r] + people[l] > limit:
                r-=1
                count +=1
            elif people[r] + people[l] <= limit:
                l+=1
                r-=1
                count +=1
            else:
                l+=1
                count+=1
        return count
        