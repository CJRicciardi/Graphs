from util import Stack

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])

    visited = []

    for _ in range(row_count):
        visited.append([False] * col_count)

    island_count = 0

    for row in range(row_count):
        for col in range(col_count):

            if not visited[row][col]:
                if islands[row][col] == 1:
                    
                    dft(row, col, islands, visited)

                    island_count += 1
    print(visited)
    return island_count

def dft(row, col, islands, visited):
    s = Stack()

    s.push((row, col))

    while s.size() > 0:
        r, c = s.pop()

        if not visited[r][c]:
            visited[r][c] = True

            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)

def get_neighbors(row, col, islands):
    neighbors = []

    if islands[row-1][col] == 1:
        neighbors.append((row-1, col))
        
    if islands[row + 1][col] == 1:
        neighbors.append((row+1, col))

    if islands[row][col-1] == 1:
        neighbors.append((row, col-1))

    if islands[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors

print(island_counter(islands))