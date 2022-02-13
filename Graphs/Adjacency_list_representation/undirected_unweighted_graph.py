
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

