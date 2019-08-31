

adjacents={}
walls=set()
non_terminals=[]

f=open("input.txt", "r")
N=int(f.readline().rstrip())
grid=[[-99999 for x in range(N)] for y in range(N)]
policy=[['' for p in range(N)] for q in range(N)]

M=int(f.readline().rstrip())
for i in range(M):
    coordinates=f.readline().rstrip().split(",")
    rows=int(coordinates[0])-1
    cols=int(coordinates[1])-1
    grid[rows][cols]=float('-inf')
    policy[rows][cols]='N'
    walls.add((rows,cols))

T=int(f.readline())
for i in range(T):
    coordinates=f.readline().rstrip().split(",")
    rows=int(coordinates[0])-1
    cols=int(coordinates[1])-1
    grid[rows][cols]=float(coordinates[2])
    policy[rows][cols] = 'E'

P=float(f.readline().rstrip())
Q=float(0.5 * (1 - P))
Rp=float(f.readline().rstrip())
gamma=float(f.readline().rstrip())
# epsilon=float(0.01* (1-gamma)/gamma)

for i in range(N):
    for j in range(N):
        if grid[i][j]== -99999:
            grid[i][j]=Rp
            non_terminals.append((i,j))

def move_up(x,y):
    up = 0.0
    current = 0.0
    left_up = 0.0
    right_up = 0.0
    temp = adjacents[(x, y)]
    if temp['up'] != None: up = P
    else: current += P
    if temp['left_up'] != None: left_up = Q
    else: current += Q
    if temp['right_up'] != None: right_up = Q
    else: current += Q
    up_utility=current*grid[x][y]
    if temp['up'] != None:
        coords=temp['up']
        up_utility+=up*grid[coords[0]][coords[1]]
    if temp['left_up'] != None:
        coords=temp['left_up']
        up_utility+=left_up*grid[coords[0]][coords[1]]
    if temp['right_up'] != None:
        coords=temp['right_up']
        up_utility+=right_up*grid[coords[0]][coords[1]]

    down = 0.0
    current = 0.0
    left_down = 0.0
    right_down = 0.0
    if temp['down'] != None: down = P
    else: current += P
    if temp['left_down'] != None: left_down = Q
    else: current += Q
    if temp['right_down'] != None: right_down = Q
    else: current += Q
    down_utility=current*grid[x][y]
    if temp['down'] != None:
        coords=temp['down']
        down_utility+=down*grid[coords[0]][coords[1]]
    if temp['left_down'] != None:
        coords=temp['left_down']
        down_utility+=left_down*grid[coords[0]][coords[1]]
    if temp['right_down'] != None:
        coords=temp['right_down']
        down_utility+=right_down*grid[coords[0]][coords[1]]

    left = 0.0
    current = 0.0
    left_down = 0.0
    left_up = 0.0
    if temp['left'] != None: left = P
    else: current += P
    if temp['left_down'] != None: left_down = Q
    else: current += Q
    if temp['left_up'] != None: left_up = Q
    else: current += Q
    left_utility=current*grid[x][y]
    if temp['left'] != None:
        coords=temp['left']
        left_utility+=left*grid[coords[0]][coords[1]]
    if temp['left_up'] != None:
        coords=temp['left_up']
        left_utility+=left_up*grid[coords[0]][coords[1]]
    if temp['left_down'] != None:
        coords=temp['left_down']
        left_utility+=left_down*grid[coords[0]][coords[1]]

    right = 0.0
    current = 0.0
    right_down = 0.0
    right_up = 0.0

    if temp['right'] != None: right = P
    else: current += P
    if temp['right_down'] != None: right_down = Q
    else: current += Q
    if temp['right_up'] != None: right_up = Q
    else: current += Q
    right_utility=current*grid[x][y]
    if temp['right'] != None:
        coords=temp['right']
        right_utility+=right*grid[coords[0]][coords[1]]
    if temp['right_up'] != None:
        coords=temp['right_up']
        right_utility+=right_up*grid[coords[0]][coords[1]]
    if temp['right_down'] != None:
        coords=temp['right_down']
        right_utility+=right_down*grid[coords[0]][coords[1]]

    return up_utility*gamma, down_utility*gamma, left_utility*gamma, right_utility*gamma


def compute_adjacents():
    for (row,col) in non_terminals:
        adjacents[(row,col)]={}
        if row-1 >= 0 and row-1 < N and col >= 0 and col < N and (row-1,col) not in walls:
            adjacents[(row, col)]['up']=(row-1,col)
        else: adjacents[(row, col)]['up']=None
        if row+1 >= 0 and row+1 < N and col >= 0 and col < N and (row+1,col) not in walls:
            adjacents[(row, col)]['down']=(row+1,col)
        else: adjacents[(row, col)]['down']=None
        if row >= 0 and row < N and col-1 >= 0 and col-1 < N and (row,col-1) not in walls:
            adjacents[(row, col)]['left']=(row,col-1)
        else: adjacents[(row, col)]['left']=None
        if row >= 0 and row < N and col+1 >= 0 and col+1 < N and (row,col+1) not in walls:
            adjacents[(row, col)]['right']=(row,col+1)
        else: adjacents[(row, col)]['right']=None
        if row-1 >= 0 and row-1 < N and col-1 >= 0 and col-1 < N and (row-1,col-1) not in walls:
            adjacents[(row, col)]['left_up']=(row-1,col-1)
        else: adjacents[(row, col)]['left_up']=None
        if row+1 >= 0 and row+1 < N and col-1 >= 0 and col-1 < N and (row+1,col-1) not in walls:
            adjacents[(row, col)]['left_down'] = (row + 1, col - 1)
        else: adjacents[(row, col)]['left_down']=None
        if row-1 >= 0 and row-1 < N and col+1 >= 0 and col+1 < N and (row-1,col+1) not in walls:
            adjacents[(row, col)]['right_up']=(row-1,col+1)
        else: adjacents[(row, col)]['right_up']=None
        if row+1 >= 0 and row+1 < N and col+1 >= 0 and col+1 < N and (row+1,col+1) not in walls:
            adjacents[(row, col)]['right_down']=(row+1,col+1)
        else: adjacents[(row, col)]['right_down']=None


def main():
    compute_adjacents()
    flag=True
    diff = 1.0

    while(flag and diff> 0.00000006):
        diff = 0.0
        flag = False
        for (i,j) in non_terminals:
            actions_utility = {}
            up_val,down_val,left_val,right_val=move_up(i,j)
            actions_utility[up_val]='U'
            actions_utility[down_val]='D'
            actions_utility[left_val]='L'
            actions_utility[right_val]='R'

            utility = max(actions_utility)
            action = actions_utility[utility]

            policy[i][j] = action
            if grid[i][j] < utility + Rp:
                diff = max(diff, abs(grid[i][j] - (utility + Rp)))
                grid[i][j] = utility + Rp
                flag=True

    f=open("output.txt","w")
    for row in range(N):
        for col in range(N):
            f.write("%s" %policy[row][col])
            if col!=N-1: f.write(",")
        f.write("\n")


if __name__ == "__main__": 
    main()
