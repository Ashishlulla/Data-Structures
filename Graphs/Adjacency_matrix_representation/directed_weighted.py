nodes =[]
graph = []
node_count = 0
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "Node is already present")
    else:
        node_count +=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edges(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "Node is not present")
    elif v2 not in nodes:
        print(v2, "Node is not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost

        
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"Node is Not present")
    else:
        index1 = nodes.index(v)
        node_count -= 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1, v2):
    if v1 is not nodes:
        print(v1, "Not present in Graph")
    elif v2 is not nodes:
        print(v2, "Not present in Graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0        
        

def print_grapgh():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"),end=" ")
        print("\n")        
        
