class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        track = {}
        for i in nums1:
            track[i] = 1 + track.get(i,0)
        
        ans = []

        for i in nums2:
            if i in track and track[i] > 0:
                ans.append(i)
                track[i] -=1
        
        return ans