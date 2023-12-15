class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        track = {}

        for path in paths:
            if path[0] not in track:
                track[path[0]] = path[1]
            else:
                continue

        for path in paths:
            if path[1] not in track:
                return path[1]


        