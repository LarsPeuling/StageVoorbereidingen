import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
        
    print("Commands: \n 'w' - up \n 's' - down \n 'a' - left \n 'd' - right \n 'e' - exit")
    return mat

def findEmpty(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return (i, j)
    return None, None

def addNew2(mat):
    
    if all(all(cell != 0 for cell in row) for row in mat):
        return
    
    tries = 0
    while tries < 30:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            return
        
        tries += 1
    
    r,c = findEmpty(mat)
    
    if r is not None and c is not None:
        mat[r][c] = 2
        
        
def getCurrentGameState(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
            
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
            
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

def compress(mat):
    changed = False
    new_mat = []
    
    for i in range(4):
        new_mat.append([0] * 4)
        
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
                
    return new_mat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
        
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[i][3-j]
            
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
            
    return new_mat

def moveLeft(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2, = merge(new_grid)
    changed = changed1 or changed2
    
    new_grid, temp = compress(new_grid)
    return new_grid, changed

def moveRight(grid):
    new_grid = reverse(grid)
    new_grid, changed = moveLeft(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def moveUp(grid):
    new_grid = transpose(grid)
    new_grid, changed = moveLeft(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def moveDown(grid):
    new_grid = transpose(grid)
    new_grid, changed = moveRight(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed