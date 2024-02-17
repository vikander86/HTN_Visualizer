from .map import *
"""
OPERATORS
"""


def move_to(state, destination):
    """
    For moving agent from one node to another

    Args:
        state (State): current state
        agent (str): the agent performing the action
        destination (str): the destination of the agent

    Returns:
        state: With updated position
    """
    if room_of(state.pos) == room_of(destination):

        state.pos = destination
        return state
    else:
        return False


def cross_door(state, door, door_node):
    """
    Crossing doorway action.

    Args:
        state (State): current state
        agent (str): the agent performing the action
        door (str): the door to cross

    Returns:
        state: with agent moving to the opposit side of the door
    """
    current_node = state.pos
    if door_node == other_side_of(door, room_of(current_node)):
        state.pos = other_side_of(door, room_of(current_node))
        return state
    else:
        return False


def open_door(state, door):
    """
    Open door

    Args:
        state (State): current state
        door (str): the door to open

    Returns:
        State: state with door now open
    """
    if state.door[door] == "closed":
        state.door[door] = "open"
        return state
    else:
        return False


def close_door(state, door):
    """
    Open door

    Args:
        state (State): current state
        door (str): the door to close

    Returns:
        State: state with door now closed
    """
    if state.door[door] == "open":
        state.door[door] = "closed"
        return state
    else:
        return False


def pickup(state, box):
    """
    Pick up box

    Args:
        state (State): current state
        box (str): the box to pickup
    Returns:
        State: state with box now holding
    """
    # If not holding box, set holding to box
    if state.holding == False:
        if state.pos == state.box[box]:
            state.holding = box
            return state
    else:
        return False


def drop(state, box):
    """
    Pick up box

    Args:
        state (State): current state
        box (str): the box to drop
    Returns:
        State: state with no longer holding box
    """
    # If holding box, set holding to False
    if state.holding == box:
        state.box[box] = state.pos
        state.holding = False
        return state
    else:
        return False
