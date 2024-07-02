class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #Approach 2 - After sorting
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans


# TC - O(M+N)
# SC - O(min(M,N)) where K is the len of either nums1 or nums2
        # track = {}
        # for i in nums1:
        #     track[i] = 1 + track.get(i,0)
        
        # ans = []

        # for i in nums2:
        #     if i in track and track[i] > 0:
        #         ans.append(i)
        #         track[i] -=1
        
        # return ans