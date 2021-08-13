def mineSweeper(bombs, num_rows, num_columns):
    field = []
    for count in range(num_rows):
        row_lst = [0] * num_columns
        field.append(row_lst)
        row_lst = []
    
    
    bomb_surrounding = []
    for bomb_coordinates in bombs:
        row, col = bomb_coordinates
        
        field[row][col] = -1
        left = [row, max(col - 1, 0)]
        right = [row, min(col + 1, num_columns - 1)]
        top = [max(row - 1, 0), col]
        bottom = [min(row + 1, num_rows - 1), col]
        top_right = [max(row - 1, 0), min(col + 1, num_columns - 1)]
        top_left = [max(row - 1, 0), max(col - 1, 0)]
        bottom_right = [min(row + 1, num_rows - 1), min(col + 1, num_columns - 1)]
        bottom_left = [min(row + 1, num_rows - 1), max(col - 1, 0)]
            
        bomb_surrounding.extend([left, right, top, bottom, top_right, top_left, bottom_right, bottom_left])
        
        
    seen = {}
    count = 0
    for coordinate in bomb_surrounding:
        row, column = coordinate
        count += 1
        
        if field[row][column] != -1 and str(coordinate) not in seen:
            field[row][column] += 1
            seen[str(coordinate)] = coordinate
        
        if count == 8:
            count = 0
            seen = {}
        
        
    return "\n".join(str(row) for row in field)


print(mineSweeper([[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]], 5, 5))