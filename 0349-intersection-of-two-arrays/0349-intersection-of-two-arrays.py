class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        track = {}
        for i in nums1:
            track[i] = 1 +  track.get(i,0)

        ans = set()
        for i in nums2:
            if i in track:
                ans.add(i)

        return ans


        