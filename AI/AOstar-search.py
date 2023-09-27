import heapq
import numpy as np

def a_star(graph, start, goal):
    # Initialize the open and closed sets
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f-score, node)
    came_from = {}  # to keep track of the path
    g_score = {node: float('inf') for node in graph}  # actual cost from start to node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # estimated total cost from start to goal
    f_score[start] = heuristic(start, goal)  # heuristic function to estimate cost

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def heuristic(node, goal):
    #setting hueristic function equal to manhattan distance
    return np.abs(convert(node) - convert(goal))
    
def ao_star(graph, start, goal, max_iterations):
    best_path = None
    best_cost = float('inf')
    
    for i in range(max_iterations):
        path = a_star(graph, start, goal)
        
        if path is not None:
            cost = calculate_path_cost(graph, path)
            
            if cost < best_cost:
                best_path = path
                best_cost = cost
        
        if i == max_iterations - 1:
            break
        
        graph = update_graph(graph, path)
        
        if a_star(graph, start, goal)==None:
            print('Skipping further iterations as no further optimisation possible.....')
            break
    
    return best_path

def calculate_path_cost(graph, path):
    cost = 0
    
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    
    return cost

def update_graph(graph, path):
    updated_graph = graph.copy()
    
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i+1]
        
        if node2 in updated_graph[node1]:
            del updated_graph[node1][node2]
    
    return updated_graph
    
def convert(string):
    if string=='A':
        return 1
    elif string=='B':
        return 2
    elif string=='C':
        return 3
    elif string=='D':
        return 4
    elif string=='E':
        return 5
    else:
        return 6

# Example graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 4, 'E': 6},
    'D': {'F': 1},
    'E': {'F': 8},
    'F': {}
}

print('Empty Graph initiated having 6 vertices.....')
graph = {'A':{}, 'B':{}, 'C':{}, 'D':{}, 'E':{}, 'F':{}}
keyslist = graph.keys()
print('Graph node format is ', list(keyslist))
while(1):
    a, b, w = input('Enter edge having weight w between vertices:-').split()
    if a not in keyslist or b not in keyslist:
        raise AttributeError('Invalid Node vertex/vertices')
    graph[a][b] = int(w)
    op = bool(int(input('Want to continue(0/1):-')))
    if op==False:
        break

a, b = input('Enter start and goal vertex:-').split()

start_node = a
goal_node = b

n = int(input('Enter maximum number of iterations to be performed:-'))

path = ao_star(graph, start_node, goal_node, n)
print("Path:", path)