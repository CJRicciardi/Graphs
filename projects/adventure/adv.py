from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def inverse(d):
    # n, e, s, w

    if d == 'n':
        return 's'
    elif d == 'e':
        return 'w'
    elif d == 's':
        return 'n'
    else:
        return 'e'

def bft(start):
    """
    Takes the starting room, and finds the nearest room with a ? in 
    the directions dict.
    Returns the path to the nearest room with a ? in the directions.
    """
    q = Queue()

    local = {}  # Note that this is a dictionary, not a set

    q.enqueue([start])

    global visited

    found = False

    while found == False:
        path = q.dequeue()

        u = path[-1]

        if u not in local:
            local[u] = path

            for key, val in visited[u].items():
                path_copy = list(path)
                path_copy.append(val)
                q.enqueue(path_copy)
                if val == '?':
                    direction = key
                    destination = u
                    return local[u], direction



    # return local

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = {}

# s = Stack()

# s.push(player.current_room.id)


# visited[player.current_room.id] = {}

# create empty visited dict
# create stack
# add current room to stack
# while loop:
    # remove top item from stack
    # if current not in visited, add it, and for loop through exits to add to available options for that room in visited
    # add first unused option to directions
    # add opposite direction to out
    # move in the direction of the first option
v = player.current_room.id
counter = 0
test = True
direction = None
lastroom = None
lastmove = None
# while len(visited) < len(room_graph):
# while test == True:
while counter < 30:

    # if previous != None:
    #     visited[player.current_room.id][inverse(direction)] = previous
    #     print('ran previous')

    counter += 1
    print('\n\ncount:', counter, '\n')

    # v = s.pop()
    print('\nv!!!!!:', v)

    if v not in visited.keys():
        visited[player.current_room.id] = {}

        for d in player.current_room.get_exits():
            visited[player.current_room.id][d] = '?'

        for nesw, room in visited[player.current_room.id].items():
            if room == '?':
                if direction == inverse(nesw):
                    pass
                else:
                    direction = nesw
                    traversal_path.append(direction)
                    # out.append(inverse(direction))
                    previous = player.current_room.id
                    # print(previous)
                    player.travel(direction)
                    # s.push(player.current_room.id)
                    v = player.current_room.id
                    current = player.current_room.id
                    visited[previous][direction] = player.current_room.id
                    # visited[current][inverse(direction)] = previous
                    print('\nno v', '\nvisited:', visited, '\ncurrent:', current, '\nv:', v)  #, '\ntraversal path:', traversal_path)
                    break

    else:
        if '?' not in visited[current].values():
            print('bft current:', current)
            path, direction = bft(current)
            # print('no ?', path, direction)
            for i in range(len(path)):
                for nesw, room in visited[i].items():
                    if room == i:
                        print(' loop 1')
                        previous = player.current_room.id
                        player.travel(nesw)
                        traversal_path.append(nesw)
                        visited[previous][nesw] = player.current_room.id
                        current = v = player.current_room.id
            player.travel(direction)
            traversal_path.append(direction)
            current = v = player.current_room.id
            for nesw, room in visited[current].items():
                if room == '?':
                    previous = player.current_room.id
                    player.travel(nesw)
                    traversal_path.append(nesw)
                    visited[previous][nesw] = player.current_room.id
                    current = v = player.current_room.id
                    print(' loop 2')
                    break
            print('\nno ?', '\nvisited:', visited, '\ncurrent:', current, '\nv:', v) 
        else:
            # print('? loop')
            for nesw, room in visited[current].items():
                if room == '?':
                    previous = player.current_room.id
                    direction = nesw
                    player.travel(nesw)
                    traversal_path.append(nesw)
                    visited[previous][nesw] = player.current_room.id
                    current = v = player.current_room.id
                    break
            print('\n? loop', '\nvisited:', visited, '\ncurrent:', current, '\nv:', v) 


        # print('\n\ncurrent:', player.current_room.id, '\ndirection:', direction) #, '\ntraversal_path:', traversal_path)
    if lastmove == None:
        lastmove = direction
        lastroom = previous
    else:
        print('\nlast move:', lastmove, 'lastroom:', lastroom)
        visited[previous][inverse(lastmove)] = lastroom
        lastmove = direction
        lastroom = previous
        print('direction:', direction, 'previous:', previous)

        test = False


print(visited)
print(current)
##############################################
# notes
##############################################
# player.current_room.id  => 0

# player.current_room.get_exits() => ['n', 's', 'e', 'w']

# player.travel(direction)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
