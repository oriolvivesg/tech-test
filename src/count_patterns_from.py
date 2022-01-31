# Lista de los posibles movimientos horizontales, verticales y diagonales sin sobrepasar ningún punto
G = {
    'a': set('bde'),
    'b': set('acfef'),
    'c': set('bef'),
    'd': set('abehg'),
    'e': set('abcdfghi'),
    'f': set('bcehi'),
    'g': set('deh'),
    'h': set('defgi'),
    'i': set('efh')
}

""" Lista de los posibles movimientos horizontales, verticales y diagonales sobrepasando algún punto
Ejemplo: a es el nodo desde el cual debe de estar, b es el punto que debe estar marcado y 
c sera el que puede ser marcado ahora
"""

S = {
    'a': {
        'b': set('c'),
        'd': set('g'),
        'e': set('i')
    },
    'b': {
        'e': set('h')
    },
    'c': {
        'f': set('i'),
        'b': set('a'),
        'e': set('g')
    },
    'd': {
        'e': set('f')
    },
    'f': {
        'e': set('d')
    },
    'g': {
        'd': set('a'),
        'e': set('c'),
        'h': set('i')
    },
    'h': {
        'e': set('b')
    },
    'i': {
        'h': set('g'),
        'e': set('a'),
        'f': set('c')
    }
}

marked = {}


def count_patterns(node, length):

    if length == 1:
        return len(G[node])
    result = 0
    neighbors = G[node]

    if node in S:
        for node_element in S[node]:
            if marked[node_element]:
                neighbors = neighbors.union(S[node][node_element])

    for neighbor in neighbors:
        if not marked[neighbor]:
            marked[neighbor] = True
            result += count_patterns(neighbor, length - 1)
            marked[neighbor] = False
    return result


def count_patterns_from(first_point, length):
    nodes = "a|b|c|d|e|f|g|h|i"
    nodes_array = nodes.split("|")

    if isinstance(first_point, int) or not isinstance(length, int):
        return "First Point debe ser una letra de la A a la I. Length debe de ser un entero del 1 al 9"
    first_point = first_point.lower()

    if first_point not in nodes_array or length > 9 or length < 1:
        return "Las letras son abcdefghi, la longitud debe de ser entre 1 y 9"

    first_point = first_point.lower()
    global marked
    marked = {}

    for node in nodes_array:
        marked[node] = False
    return count_patterns(first_point, length)


total = 0
for number in range(1, 10):
    for element in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
        total += count_patterns_from(element, number)

print(total)