def is_valid_sudoku(board, custom_zones):
    def is_valid_group(group):
        return sorted(group) == list(range(1, 10))

    for row in board:
        if not is_valid_group(row):
            return False

    for col in zip(*board):
        if not is_valid_group(list(col)):
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = [board[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            if not is_valid_group(box):
                return False

    for zone in custom_zones:
        zone_vals = [board[i][j] for (i, j) in zone]
        if not is_valid_group(zone_vals):
            return False

    return True

# 🧪 Test
board = [[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,9]]
zones = [[(i, j) for j in range(9)] for i in range(9)]
print("Valid Sudoku with Zones:", is_valid_sudoku(board, zones))  # True
