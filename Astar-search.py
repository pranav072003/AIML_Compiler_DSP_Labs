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

path = a_star(graph, start_node, goal_node)
print("Path:", path)