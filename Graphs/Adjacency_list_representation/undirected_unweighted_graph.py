
graphdict = {}
# visited = set()

def add_node(v):
    if v in graphdict:
        print(v, "Node is Already present")
    else:
        graphdict.update({v:[]})

def add_edge(v1,v2):
    if v1 not in graphdict:
        print(v1, "Node not present in Graph")
    elif v2 not in graphdict:
        print(v2, "Node not present in Graph")
    else:
        graphdict[v1].append(v2)
        graphdict[v2].append(v1)

def delete_node(v):
    if v not in graphdict:
        print(v,"Not present in Graph")
    else:
        graphdict.pop(v)
        for i in graphdict.values():
            if v in i:
                i.remove(v)
            else:
                pass


def delete_edge(v1,v2):
    if v1 not in graphdict:
        print(v1, "Node not present in Graph")
    elif v2 not in graphdict:
        print(v2, "Node not present in Graph")
    else:
        if v2 in graphdict[v1]:
            graphdict[v1].remove(v2)
            graphdict[v2].remove(v1)
        else:
            pass

# def DFS_recursive(node, visited, graphdict):
#     if node in graphdict:
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             for i in graphdict[node]:
#                 DFS(i, visited, graphdict)
#     else:
#         print("Node is not Present")


def DFS_iterative(node, graphdict):
    visited = set()
    if node not in graphdict:
        print("Node is not present")
        return
    stack = []
    stack.append(node)
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for i in graphdict[curr]:
                stack.append(i)





# -----------------Adding Nodes ------------------------
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

#----------------- Adding Edges -----------------------

add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")

print(graphdict)

# DFS_recursive("A", visited, graphdict)
DFS_iterative("A", graphdict)
# --------------------- Deleting Node --------------------

# delete_node("A")
# delete_edge("A","B")

# print("After Deleting")
# print(graphdict)
