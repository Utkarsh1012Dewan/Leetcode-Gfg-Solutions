class Solution:
    def minOperations(self, logs: List[str]) -> int:

        count = 0

        for i in logs:
            if i == "./":
                continue
            elif i == "../" and count > 0:
                count -=1
            elif i[0].isalnum():
                count +=1
        
        return count
        