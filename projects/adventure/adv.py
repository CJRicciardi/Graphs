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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}


exit_path = []

inverse_direction = {"n":"s", "e":"w", "s":"n", "w":"e"}

visited[player.current_room.id] = player.current_room.get_exits()

#figure out loop for visited list vs list of 500 rooms
while len(visited) < len(room_graph):
    # in a new rom:
        # add room and directions to visited
        # then remove the direction you came from
    if player.current_room.id not in visited:  
        visited[player.current_room.id] = player.current_room.get_exits() 
        direction = exit_path[-1]
        visited[player.current_room.id].remove(direction)

    # in a room with exhausted directions:
        # go back in the direction you came from
        # remove the exit_path step you just took
    if len(visited[player.current_room.id]) == 0:
        direction = exit_path.pop()
        traversal_path.append(direction)
        player.travel(direction)

    else:
    # in a room with unexplored directions:
        # head in an unexplored direction
        # remove the direction you will go from the room
        # update traversal_path
        # update exit_path
        direction = visited[player.current_room.id].pop()
        traversal_path.append(direction)
        exit_path.append(inverse_direction[direction])
        player.travel(direction)

#figure out what to do when you hit a deadend. a room where all paths have been discovered.
#backtrack until you encounter a room with paths that have not been discovered


# TRAVERSAL TEST
visited = set()
player.current_room = world.starting_room
visited.add(player.current_room)

# get the first room and exits added to the visited
#

for move in traversal_path:
    player.travel(move)
    visited.add(player.current_room)

if len(visited) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited)} unvisited rooms")



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