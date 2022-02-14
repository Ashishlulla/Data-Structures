
graphdict = {}
visited = set()

def add_node(v):
    if v in graphdict:
        print(v, "Node is Already present")
    else:
        graphdict.update({v:[]})

def add_edge(v1,v2, cost):
    if v1 not in graphdict:
        print(v1, "Node not present in Graph")
    elif v2 not in graphdict:
        print(v2, "Node not present in Graph")
    else:
        graphdict[v1].append([v2, cost])
        graphdict[v2].append([v1, cost])

def delete_node(v):
    if v not in graphdict:
        print(v,"Not present in Graph")
    else:
        graphdict.pop(v)
        for i in graphdict.values():
            for j in i:
                if v == j[0]:
                    i.remove(j)
                    break

def delete_edge(v1,v2, cost):
    if v1 not in graphdict:
        print(v1, "Node not present in Graph")
    elif v2 not in graphdict:
        print(v2, "Node not present in Graph")
    else:
        temp = [v1,cost]
        temp1 = [v2, cost]
        if temp1 in graphdict[v1]:
            graphdict[v1].remove(temp1)
            graphdict[v2].remove(temp)
            
        else:
            pass

def DFS(node, visited, graphdict):
    if node not in graphdict:
        print("Node is Not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graphdict[node]:
            DFS(i[0], visited, graphdict)




# -----------------Adding Nodes ------------------------
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")

#----------------- Adding Edges -----------------------

add_edge("A", "B",10)
add_edge("C", "D",20)
add_edge("E", "F",30)
add_edge("A", "F",40)
add_edge("B", "C",50)


print(graphdict)
DFS("A",visited, graphdict)
delete_node("A")
print(graphdict)
