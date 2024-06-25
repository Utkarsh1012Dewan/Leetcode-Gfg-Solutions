class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def get_neighbours(coord):
            res = []
            row,col = coord
            row_index = [-1,0,1,0]
            col_index = [0,1,0,-1]
            for i in range(len(row_index)):
                new_r = row + row_index[i]
                new_c = col + col_index[i]

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    res.append((new_r,new_c))
            return res

        def bfs(start):
            queue = deque([start])
            r,c = start
            grid[r][c] = '0'
            while len(queue) > 0:
                node = queue.popleft()
                for neighbour in get_neighbours(node):
                    r1,c1 = neighbour
                    if grid[r1][c1] == '0':
                        continue
                    queue.append(neighbour)
                    grid[r1][c1] = '0'

        count = 0
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                bfs((r,c))
                count +=1
        return count

        