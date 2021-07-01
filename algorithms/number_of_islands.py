def numIslands(grid):
    num_islands = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row_idx in range(0, num_rows):
        for col_idx in range(0, num_cols):
            if grid[row_idx][col_idx] == "1":
                num_islands += 1
                BFSearch_Land(grid, num_rows, num_cols, row_idx, col_idx)

    return num_islands

def BFSearch_Land(grid, num_rows, num_cols, row_idx, col_idx):
    matrix_idx = create_matrix_idx(row_idx, col_idx, num_cols)
    queue = [matrix_idx]

    while len(queue) != 0:
        popped = queue.pop(0)
        popped_row_idx = popped // num_cols
        popped_col_idx = popped % num_cols

        if (popped_col_idx - 1 >= 0) and grid[popped_row_idx][popped_col_idx - 1] == "1": 
                queue.append(create_matrix_idx(popped_row_idx, popped_col_idx - 1, num_cols)) 
                grid[popped_row_idx][popped_col_idx - 1] = "0"
        if (popped_col_idx + 1 < num_cols) and grid[popped_row_idx][popped_col_idx + 1] == "1":
                queue.append(create_matrix_idx(popped_row_idx, popped_col_idx + 1, num_cols))
                grid[popped_row_idx][popped_col_idx + 1] = "0"
        if (popped_row_idx - 1 >= 0) and grid[popped_row_idx - 1][popped_col_idx] == "1":
                queue.append(create_matrix_idx(popped_row_idx - 1, popped_col_idx, num_cols))
                grid[popped_row_idx - 1][popped_col_idx] = "0"
        if (popped_row_idx + 1 < num_rows) and grid[popped_row_idx + 1][popped_col_idx] == "1":
                queue.append(create_matrix_idx(popped_row_idx + 1, popped_col_idx, num_cols))
                grid[popped_row_idx + 1][popped_col_idx] = "0"
    
def create_matrix_idx(row_idx, col_idx, num_cols):
    return (row_idx * num_cols) + col_idx


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

print(numIslands(grid))