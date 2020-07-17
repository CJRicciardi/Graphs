def dft(self, starting_vertex_id):
    # Create an empty stack
    s = Stack()

    # Create a set to store the visited nodes
    visited = set()

    # Init: push the starting node
    s.push(starting_vertex_id)

    # While the stack isn't empty
    while s.size() > 0:
        # pop the first item
        v = s.pop()
        # If it's not been visited:
        if v not in visited:
            # Mark as visited (i.e. add to the visited set)
            visited.add(v)

            # Do something with the node
            print(f"Visited {v}")

            # Add all neighbors to the stack
            for next_vert in self.get_neighbors(v):
                s.push(next_vert)

def bft(self, starting_vertex_id):
    # Create an empty queue
    q = Queue()

    # Create a set to store the visited nodes
    visited = set()

    # Init: enqueue the starting node
    q.enqueue(starting_vertex_id)

    # While the queue isn't empty
    while q.size() > 0:
        # Dequeue the first item
        v = q.dequeue()
        # If it's not been visited:
        if v not in visited:
            # Mark as visited (i.e. add to the visited set)
            visited.add(v)

            # Do something with the node
            print(f"Visited {v}")

            # Add all neighbors to the queue
            for next_vert in self.get_neighbors(v):
                q.enqueue(next_vert)

def get_all_social_paths(self, user_id):
    """
    Takes a user's user_id as an argument

    Returns a dictionary containing every user in that user's
    extended network with the shortest friendship path betweenthem.

    The key is the friend's ID and the value is the path.
    """
    q = Queue()

    visited = {}  # Note that this is a dictionary, not a set

    q.enqueue([user_id])

    while q.size() > 0:
        path = q.dequeue()

        u = path[-1]

        if u not in visited:
            visited[u] = path

            for neighbor in self.friendships[u]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return visited

