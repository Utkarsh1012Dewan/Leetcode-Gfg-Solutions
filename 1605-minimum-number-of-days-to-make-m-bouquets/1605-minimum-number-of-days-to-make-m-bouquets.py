class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m*k > len(bloomDay) : return -1

        minVal,maxVal = min(bloomDay),max(bloomDay)
        low,high = minVal,maxVal

        while low<=high:
            mid = (low+high)//2

            if self.possible(bloomDay,mid,m,k):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

    def possible(self,arr,mid,m,k):
        count = 0
        bouquet = 0

        for i in range(len(arr)):
            if arr[i] <= mid:
                count+=1
            else:
                bouquet += count//k
                count = 0
        bouquet += count//k
        return bouquet >= m
        