from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # build the family tree
    print('\n')
    tree = {}
    for i in range(len(ancestors)):
        if ancestors[i][1] not in tree.keys():
            tree[ancestors[i][1]] = set()
            tree[ancestors[i][1]].add(ancestors[i][0])
        else:
            tree[ancestors[i][1]].add(ancestors[i][0])

    # key = child, value = parent
    # print(tree)

    s = Stack()
    visited = set()
    s.push(starting_node)
    visitList = []
    anstack = Stack()

    while s.size() > 0:
        v = s.pop()
        # print(v)
        
        if v not in visited:
            visited.add(v)
            anstack.push(v)
            # print(v)
            if v not in tree.keys():
                pass
            else:
                for next_vert in tree[v]:
                    s.push(next_vert)
            

    a = anstack.pop()
    b = anstack.pop()

    if a == starting_node:
        return - 1
    elif b is None:
        return a
    # elif a > b:
    #     # return b, a
    #     if (a & b) not in tree.keys():
    #         return a
    #     else:
    #         return b
    elif a not in tree.keys() and b not in tree.keys():
        # return b, a
        if a > b:
            return b
        else:
            return a
    else:
        return a



if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 2)) # -1
    print(earliest_ancestor(test_ancestors, 3)) # 10
    print(earliest_ancestor(test_ancestors, 5)) # 4
    print(earliest_ancestor(test_ancestors, 7)) # 4
    print(earliest_ancestor(test_ancestors, 8)) # 4
    print(earliest_ancestor(test_ancestors, 9)) # 4
    print(earliest_ancestor(test_ancestors, 10))# -1
    print(earliest_ancestor(test_ancestors, 11))# -1

#  {3: {1, 2}, 6: {3, 5}, 7: {5}, 5: {4}, 8: {11, 4}, 9: {8}, 1: {10}}
    