class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        track = {}
        for i in nums[0]:
            track[i] = 1

        for i in nums:
            cnt = Counter(i)
            for i in track:

                track[i] = min(track[i],cnt[i])

        res = []

        for i in track:
            if track[i] > 0:
                res.append(i)
        res.sort()
        return res
        