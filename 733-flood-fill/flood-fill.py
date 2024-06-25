class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        def get_neighbours(coord,color):
            row,col = coord
            row_index = [-1,0,1,0]
            col_index = [0,1,0,-1]
            for i in range(len(row_index)):
                new_row = row + row_index[i]
                new_col = col + col_index[i]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if image[new_row][new_col] == color:
                        yield new_row,new_col
        def bfs(root):
            queue = deque([root])
            visited = [[False for j in range(cols)] for i in range(rows)]
            r,c = root
            old_color = image[r][c]
            image[r][c] = color
            visited[r][c] = True

            while (len(queue)) > 0:
                node = queue.popleft()
                for neighbour in get_neighbours(node,old_color):
                    r,c = neighbour
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    queue.append(neighbour)
                    visited[r][c] = True

        bfs((sr,sc))
        return image