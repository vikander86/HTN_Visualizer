"""
A simple home map, to be used for Lab4 of the "AI for HIng" course at ORU
It contains a set of rooms, a set of doors, and a set of points p1, p2, ..., pn (nodes)
Each point p is located in some room
Doors are associated with two locations, on the two sides of the door
Robot navigates between nodes, but it can only move between nodes in the same
room, or between the nodes on the two sides of a door
"""


# The map

nodes = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
         'p9', "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
rooms = {'room1': ['p1', 'p2', 'p3', "p7"],
         'room2': ['p4', 'p5', 'p6', "p15"],
         'room3': ['p8', 'p9', 'p10'],
         'room4': ['p16', 'p11', 'p13'],
         'room5': ["p12", "p14"]}
doors = {'door1': ['p3', 'p4'],
         'door2': ['p7', 'p8'],
         'door3': ['p15', 'p16'],
         'door4': ['p11', 'p12']}


def room_of(p):
    """
    Tell in what room a given node is located
    :param p: a point name (node)
    :return: a room name
    """
    for r in rooms.keys():
        if p in rooms[r]:
            return r
    return False


def side_of(d, r):
    """
    Look at the pair of nodes around a door d, and return the one which is located in room r
    :param d: a door
    :param r: a room
    :return: a node
    """
    p1, p2 = doors[d]
    if p1 in rooms[r]:
        return p1
    if p2 in rooms[r]:
        return p2
    return False


def other_side_of(d, r):
    """
    Like 'side_of' but it returns the other node
    :param d: a door
    :param r: a room
    :return: the node beside d that is located opposite to r
    """
    p1, p2 = doors[d]
    if p1 in rooms[r]:
        return p2
    if p2 in rooms[r]:
        return p1
    return False


def doors_of(r):
    """
    Returns the list of doors connected to room r
    :param r: a room
    :return: a list of doors
    """
    res = []
    for d in doors.keys():
        if side_of(d, r):
            res.append(d)
    return res


# test that the helper functions work ok

# for p in nodes:
#     print("Node", p, "is in", room_of(p))

# for d in doors:
#     for r in rooms:
#         if side_of(d, r):
#             print("Door", d, "has", side_of(d, r), "on the", r,
#                   "side, and", other_side_of(d, r), "on the other side")

# for r1 in rooms:
#     print("Room", r1, "has doors:", doors_of(r1))

