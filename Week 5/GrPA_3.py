def index_of_first_occurance(row: list, elem):
    for i in range(len(row)):
        if row[i] == elem:
            return i
    return -1

def index_of_last_occurance(row: list, elem):
    reversed_row = row[::-1]
    first_in_reversed = index_of_first_occurance(reversed_row, elem)
    if first_in_reversed == -1:
        return -1
    return len(row) - 1 - first_in_reversed

def is_valid_coordinate(x: int, y: int, M):
    return 0 <= x < len(M) and 0 <= y < len(M[0])

def valid_adjacent_coordinates(x: int, y: int, M):
    return {
        (x1, y1)
        for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        if is_valid_coordinate(x1, y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    x, y = curr_coords
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # up, left, right, down
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (is_valid_coordinate(nx, ny, M) and 
            M[nx][ny] == value and 
            (nx, ny) != prev_coords):
            return (nx, ny)
    return None

def get_path_coordinates(M):
    x_start = len(M) - 1
    y_start = index_of_last_occurance(M[-1], 1)
    if y_start == -1:
        return []

    path = []
    curr_coords = (x_start, y_start)
    prev_coords = None

    while curr_coords is not None:
        path.append(curr_coords)
        next_coords = next_coordinate_with_value(curr_coords, 1, M, prev_coords)
        prev_coords = curr_coords
        curr_coords = next_coords

    return path

def print_path(M):
    path = get_path_coordinates([row[:] for row in M])  # clone to avoid modifications
    for coord in path:
        print(coord)

def alternate_path(M):
    path = get_path_coordinates([row[:] for row in M])
    path.reverse()
    for i, (x, y) in enumerate(path):
        if i % 2 == 0:
            M[x][y] = 2
        else:
            M[x][y] = 1

def count_path(M):
    path = get_path_coordinates([row[:] for row in M])
    for i, (x, y) in enumerate(path):
        M[x][y] = i + 1

def mirror_horizontally(M):
    path = get_path_coordinates([row[:] for row in M])
    n_cols = len(M[0])
    for x, y in path:
        mirror_y = n_cols - 1 - y
        M[x][mirror_y] = 1

def mirror_vertically(M):
    path = get_path_coordinates([row[:] for row in M])
    n_rows = len(M)
    for x, y in path:
        mirror_x = n_rows - 1 - x
        M[mirror_x][y] = 1