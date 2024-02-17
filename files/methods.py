from .map import *
"""
METHODS
"""


def navigate(state, destination, visited=None):
    """
    Navigate method to move from one point to a nother, including crossing, opening, and closing doors.

    Args:
        state (State): current state
        destination (str): the destination of the agent
        visited (dict): dict containing number of visitions of visited rooms. Default to None.
    Returns:
        list: Returns a list with tasks
    """

    current_node = state.pos

    # If already at destination, return empty task list.
    if current_node == destination:
        return []
    current_room = room_of(current_node)

    # Initialize current room in visited, set to 0, if already in visited add 1
    if visited is None:
        visited = current_room
    
    # if current_room not in visited:
    #     visited = current_room

    destination_room = room_of(destination)

    # If current room is destination room, return task to move to destination.
    if current_room == destination_room:
        return [('move_to', destination)]
    else:
        # If destination is not in current room, check first through all neighbouring rooms if they are hold the destination
        for door in doors_of(current_room):
            door_node = side_of(door, current_room)
            next_room = room_of(other_side_of(door, current_room))
            next_room_node = side_of(door, next_room)
            # If next room is destination room.
            if next_room == destination_room:
                # If door is closed to destination room, return tasks including moving to door, opening, crossing and closing door, finish with navigate
                if state.door[door] == "closed":
                    return [("move_to", door_node), ("open_door", door), ("cross_door", door, next_room_node), ("close_door", door), ("navigate", destination, current_room)]
                # Else return task to destination room, return tasks including moving to door, crossing door, finish with navigate
                else:
                    return [('move_to', door_node), ('cross_door', door, next_room_node), ('navigate', destination, current_room)]
        # If destination is not any of the next room, check if room has more doors than number of times visited (to limit visiting same room recursively)
        for door in doors_of(current_room):
            door_node = side_of(door, current_room)
            next_room = room_of(other_side_of(door, current_room))
            next_room_node = side_of(door, next_room)
            if next_room not in visited or len(doors_of(current_room)) == 1:
                #If door is closed to destination room, return tasks including moving to door, opening, crossing and closing door, finish with navigate
                if state.door[door] == "closed":
                    return [("move_to", door_node), ("open_door", door), ("cross_door", door, next_room_node), ("close_door", door), ("navigate", destination, current_room)]
                # Else return task to destination room, return tasks including moving to door, crossing door, finish with navigate
                else:
                    return [('move_to', door_node), ('cross_door', door, next_room_node), ('navigate', destination, current_room)]
    return False


def fetch(state, box, visited=None):
    """
    Fetch box

    Args:
        state (State): current state
        box (str) : the box being fetched
        visited (dict): dict containing number of visitions of visited rooms. Default to None.
    Returns:
        list: Returns a list with tasks
    """
    # If not agent is not holding the box being fetched
    if state.holding != box:
        # If agent at the box, return task to pick up box.
        if state.pos == state.box[box]:
            return [("pickup", box)]
        # If agent is in the same room as box, return tasks to move to box and pick it up
        elif room_of(state.pos) == room_of(state.box[box]):
            return [("move_to", state.box[box]), ("pickup", box)]
        # If agent is NOT in the same room as box, return tasks to navigate to the box and pick it up
        else:
            return [("navigate", state.box[box], visited), ("pickup", box)]
    return []


def transport(state, box, destination, visited=None):
    """
    Transport a box to a new destination

    Args:
        state (State): current state
        destination (str): the destination of the agent
        visited (dict): dict containing number of visitions of visited rooms. Default to None.
    Returns:
        list: Returns a list with tasks
    """
    # If box is already at its destination
    if state.box[box] == destination:
        return [("fetch",box)]
    # Else return tasks to fetch box, nagivate to destination and dropping box.
    else:
        if state.holding != box:
            return [("fetch", box), ("navigate", destination, None), ("drop", box)]
        else:
            return False
