import numpy as np

def traverse(queue):
    if len(queue)==0:
        print("Queue is empty\n")
        return

    if len(queue)==1:
        print(queue[0])

    for i in range(0,len(queue)):
        print(queue[i],"\t")
      
#array=adjacent;a=vertexno        
def BFS(a, array=None):
    front_q, rear_q = -1, -1
    Q = []
    #colour=1 for white;colour=2 for grey;colour=3 for black
    colour = np.ones(a)
    i, u = 0, 1
    print("Starting from vertex ",u)
    print("\n")
    colour[0] += 1 
    print("The BFS gives traversal as:-\n")
    Q.append(u)
    while len(Q)!=0:
        p = Q[0]
        Q.pop(0)
        for i in range(0,a):
            if array[p-1][i]==True:
                if colour[i]==1:
                    colour[i]+=1 
                    Q.append(i+1)
        colour[p-1]+=1 
        print(p)

#array=adjacent;a=vertexno
def DFS(a, array=None):
    time=0
    colour = np.ones(a)
    #1 for white;2 for grey;3 for black
    j=1 
    print("Starting from vertex ",j)
    print("The DFS gives traversal as:-\n")
    print(j)
    for i in range(0,a):
        colour[i-1] = DFS_VISIT(i+1,colour,a,array);

#u=id;array=colour;size=a        
def DFS_VISIT(u, array, size, array1):
    array[u-1]+=1 
    for i in range(0,size):
        if array1[u-1][i]==True:
            if array[i]==1:
                print(i+1)
                DFS_VISIT(i+1, array, size, array1)
    array[u-1]+=1
    return array[u-1]
    
while(1):
    key = bool(int(input("Want to initialise program(0/1):-")))
    if key==False:
        break
    vertexno = int(input("Enter number of vertices of graph:-"))
    if vertexno<=0:
        print("Incorrect input")
        continue
    adjacent = np.full((vertexno,vertexno), False)
    while(1):
        a, b = input("Enter edge between vertices:-").split()
        a,b = int(a), int(b)
        if a==0 or b==0 or a>vertexno or b>vertexno:
            print("Incorrect input")
            continue
        if adjacent[a-1][b-1]==True:
            print("Already Done")
            continue
        adjacent[a-1][b-1]=True
        adjacent[b-1][a-1]=True
        key = bool(int(input("Want to continue(0/1):-")))
        if key==False:
            break
    while(1):
        choice = int(input("Want to implement DFS(1)/BFS(2)/Exit(3):-"))
        if choice==1:
            DFS(vertexno, adjacent)
        elif choice==2:
            BFS(vertexno, adjacent)
        else:
            break

print("Program Terminated")