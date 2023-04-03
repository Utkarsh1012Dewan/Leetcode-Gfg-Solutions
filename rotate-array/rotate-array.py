class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k %= n
        if k < 0:
            k+= len(nums)
        
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
        
        
        
        
    def reverse(self,nums,s,e):
        
        while s < e:
            nums[s],nums[e] = nums[e], nums[s]
            s+=1
            e-=1
        
        return nums
        