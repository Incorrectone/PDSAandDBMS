import pprint

def createAdjandinfo(maze):
    adj_list = dict() # The list
    
    # the interest points
    
    key = tuple()
    entry = tuple()
    exit = tuple()
    
    w = [' ', '*'] # walkable tiles
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'X':
                continue
            elif maze[i][j] in w:
                if maze[i][j] == '*':
                    key = (i, j)
                
                if j == 0:
                    entry = (i, j)
                    adj_list[(i, j)] = []
                    if maze[i][j+1] in w:
                        adj_list[(i, j)] = [(i, j + 1)]
                elif j > 0 and j < len(maze[0]) - 1:
                    if (i, j) not in adj_list.keys():
                        adj_list[(i, j)] = []
                        
                    try:
                        if maze[i + 1][j] in w:
                            adj_list[(i, j)].append((i + 1, j))
                    except:
                        pass
                    
                    try:
                        if maze[i - 1][j] in w:
                            adj_list[(i, j)].append((i - 1, j))
                    except:
                        pass
                    
                    try:
                        if maze[i][j + 1] in w:
                            adj_list[(i, j)].append((i, j + 1))
                    except:
                        pass
                    
                    try:
                        if maze[i][j - 1] in w:
                            adj_list[(i, j)].append((i, j - 1))
                    except:
                        pass
                elif j == len(maze[0]) - 1:
                    exit = (i, j)
                    adj_list[(i, j)] = []
                    if maze[i][j-1] in w:
                        adj_list[(i, j)] = [(i, j - 1)]
    return (adj_list, entry, exit, key)

def BFS(adj_list, source, dest):
    parent = dict()
    visited = dict()
    vertices = adj_list.keys()
    for i in vertices:
        parent[i] = -1
        visited[i] = -1
    
    stack = []
    current = source
    while(1):
        visited[current] = 1
        for i in adj_list[current]:
            if visited[i] == -1:
                parent[i] = current
                stack.append(i)
        
        if stack == [] or current == dest:
            break
        
        current = stack[0]
        del stack[0]
    parent[source] = None
    return parent

def backtrackdist(parent_dict, source):
    current = source
    dist = 0
    while(1):
        if parent_dict[current] != None:
            dist += 1
            current = parent_dict[current]
        else:
            break
    return dist        
    
    
maze = ['XXXXXXXXXXXXXX', '   X    XXX  X', 'X  X    X X  X', 'X  X         X', 'X  XX  X XX  X', 'X  X  XX  X   ', 'X     XX XXXXX', 'X  X         X', 'X  X      *  X', 'XXXXXXXXXXXXXX']
for i in range(len(maze)):
    maze[i] = list(maze[i])
    
(adj_list, entry, exit, key) = createAdjandinfo(maze)

parent1 = BFS(adj_list, entry, key)
parent2 = BFS(adj_list, key, exit)

if parent1[key] == -1:
    print(-1)
elif parent1[key] != -1 and parent2[exit] == -1:
    print(-2)
elif parent1[key] != -1 and parent2[exit] != -1:
    print(backtrackdist(BFS(adj_list, entry, key), key) + backtrackdist(BFS(adj_list, key, exit), exit))


                
                
        