class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        minEle =  min(numOnes,k)
        
        res =  1*minEle
        
        k-=numOnes
        k-=numZeros
        
        if k > 0:
            res-=k
        return res