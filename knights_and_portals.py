from collections import deque

def shortest_path(grid):
    R, C = len(grid), len(grid[0])
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    empty = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0]

    def bfs():
        visited = [[False]*C for _ in range(R)]
        q = deque([(0, 0, False, 0)])  # (r, c, used_portal, steps)
        visited[0][0] = True
        while q:
            r, c, used, d = q.popleft()
            if (r, c) == (R-1, C-1):
                return d
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==0:
                    visited[nr][nc] = True
                    q.append((nr, nc, used, d+1))
            if not used:
                for er, ec in empty:
                    if not visited[er][ec]:
                        visited[er][ec] = True
                        q.append((er, ec, True, d+1))
        return -1

    return bfs()

# 🧪 Test
grid = [[0, 1, 0], [1, 0, 1], [0, 0, 0]]
print("Shortest Path with Teleport:", shortest_path(grid))  # 3
