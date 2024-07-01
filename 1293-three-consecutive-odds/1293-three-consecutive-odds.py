class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
#My Method
        count = 0
        for i in arr:
            if i % 2 != 0:
                count +=1
                if count == 3:
                    return True
            else:
                count = 0
        return False
        

#Another clever way I looked from solutions
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
            for i in range(1, len(arr) - 1):
                if arr[i - 1] % 2 + arr[i] % 2 + arr[i + 1] % 2 == 3:
                    return True
            return False