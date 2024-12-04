from tqdm import tqdm

grid = []

with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        grid.append(list(line.strip('\n')))
print(grid)

def safe_search(grid, x, y):
    count = 0
    #up left*
    try:
        if grid[x][y] == 'X' and grid[x-1][y-1] == 'M' and grid[x-2][y-2] == 'A' and grid[x-3][y-3] == 'S' and x-3>=0 and y-3>=0:
            count+=1
            print(x, y,"upleft")
    except:
        ...
    #left*
    try:
        if grid[x][y] == 'X' and grid[x][y-1] == 'M' and grid[x][y-2] == 'A' and grid[x][y-3] == 'S'and y-3>=0:
            count+=1
            print(x, y,"left")
    except:
        ...
    #down left*
    try:
        if grid[x][y] == 'X' and grid[x+1][y-1] == 'M' and grid[x+2][y-2] == 'A' and grid[x+3][y-3] == 'S' and y-3>=0:
            count+=1
            print(x, y,'downleft')
    except:
        ...
     
        
    #up*
    try:
        if grid[x][y] == 'X' and grid[x-1][y] == 'M' and grid[x-2][y] == 'A' and grid[x-3][y] == 'S'and x-3>=0 :
            count+=1
            print(x, y,'up')
    except:
        ...
    #down*
    try:
        if grid[x][y] == 'X' and grid[x+1][y] == 'M' and grid[x+2][y] == 'A' and grid[x+3][y] == 'S':
            count+=1
            print(x, y,'down')
    except:
        ...
        
        
    #up right*
    try:
        if grid[x][y] == 'X' and grid[x-1][y+1] == 'M' and grid[x-2][y+2] == 'A' and grid[x-3][y+3] == 'S'and x-3>=0:
            count+=1
            print(x, y,'upright')
    except:
        ...
    #right*
    try:
        if grid[x][y] == 'X' and grid[x][y+1] == 'M' and grid[x][y+2] == 'A' and grid[x][y+3] == 'S':
            count+=1
            print(x, y,'right')
    except:
        ...
    #down right*
    try:
        if grid[x][y] == 'X' and grid[x+1][y+1] == 'M' and grid[x+2][y+2] == 'A' and grid[x+3][y+3] == 'S':
            count+=1
            print(x, y,'downright')
    except:
        ...
    
    return count

total = 0 
for i in range(len(grid)):
    #print(grid[i])
    print()
    for j in range(len(grid[i])):
        print(grid[i][j])
        total += safe_search(grid, i, j)

print(total)