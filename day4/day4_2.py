from tqdm import tqdm

grid = []

with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        grid.append(list(line.strip('\n')))

def safe_search(grid, x, y):
    count = 0
    #up 
    try:
        if grid[x][y] == 'A' and grid[x-1][y-1] == 'M' and grid[x+1][y-1] == 'M'\
            and grid[x+1][y+1] == 'S'and grid[x-1][y+1] == 'S' and x-1>=0 and y-1>=0:
            count+=1
    except:
        ...
    
    #left 
    try:
        if grid[x][y] == 'A' and grid[x-1][y-1] == 'M' and grid[x+1][y-1] == 'S'\
            and grid[x+1][y+1] == 'S'and grid[x-1][y+1] == 'M' and x-1>=0 and y-1>=0:
            count+=1
    except:
        ...
    #down 
    try:
        if grid[x][y] == 'A' and grid[x-1][y-1] == 'S' and grid[x+1][y-1] == 'S'\
            and grid[x+1][y+1] == 'M'and grid[x-1][y+1] == 'M' and x-1>=0 and y-1>=0:
            count+=1
    except:
        ...
    #right 
    try:
        if grid[x][y] == 'A' and grid[x-1][y-1] == 'S' and grid[x+1][y-1] == 'M'\
            and grid[x+1][y+1] == 'M'and grid[x-1][y+1] == 'S' and x-1>=0 and y-1>=0:
            count+=1
    except:
        ...
    
    return count

total = 0 
for i in range(len(grid)):
    for j in range(len(grid[i])):
        total += safe_search(grid, i, j)

print(total)