class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        a = []
        for i in range(len(names)):
            a.append((heights[i],names[i]))
        a = sorted(a,reverse=True)

        return [name for height,name in a]
        