
def zadatak1(graph, startNode):
    paths = [(startNode,)]
    queue = [(startNode,)]          #formiramo listu tuple zbog obilaska po sirini
    while queue:
        curr, *queue = queue        #spliceuje trenutni element iz queue, tj curr se izbacuje
        for node in graph[curr[-1]]:
            if node not in curr:
                paths += [(*curr, node)]     # *curr is passing all of the items in the list as separate arguments, without us even needing to know how many arguments are in the list.
                queue += [(*curr, node)]
    return (paths, max(list(map(lambda x: len(x), paths))) - 1)  #racuna dubinu tupla, n-1

graf = { 
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['A', 'B'],
    'D': ['C', 'E', 'F'],
    'E': ['G', 'H', 'A'],
    'F': ['B', 'C', 'D'],
    'G': ['E', 'H'],
    'H': ['J'],
    'J': []
}

rez = zadatak1(graf, 'A')
print('Depth is:', rez[1])