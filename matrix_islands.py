def count_islands(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)

    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1
    return count

# 🧪 Test
matrix = [[1,0,0,1],
          [0,1,1,0],
          [0,0,1,0],
          [1,0,0,1]]
print("Islands Count:", count_islands(matrix))  # 3
