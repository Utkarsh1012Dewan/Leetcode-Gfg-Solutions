class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        i = 0
        count = 0

        for j in range(2,len(colors)):
            if colors[i] == colors[j] and colors[j] != colors[j-1]:
                count+=1
            i+=1
        
        if colors[-1] == colors[1] and colors[-1] != colors[0]:
            count +=1 

        if colors[0] == colors[-2] and colors[0] != colors[-1]:
            count +=1 

        return count


        