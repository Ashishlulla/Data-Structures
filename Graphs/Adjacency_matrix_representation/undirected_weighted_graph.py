# ------------------------------- Adjacency Matrix represnetation----------------------

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
        graph[index2][index1] = cost
