from gui import Lab_4GUI
from pyhop.pyhop import *
from files import *
import random


class AppController:
    """
    Controls the application logic, interfacing between the GUI and the problem-solving algorithms.

    This controller manages user interactions, problem selection, algorithm execution, 
    and updates the GUI based on the state of the problem-solving process.
    """

    def __init__(self):
        """
        Initializes the AppController with default settings.

        Sets up the connection to the GUI, initializes variables to manage the selected algorithm,
        the current problem, the animation state, and movable entities for visualization.
        """
        self.view = Lab_4GUI(self)
        self.state1 = State("state")
        self.state1.door = {"door1": "open", "door2": "open", "door3": "open", "door4": "open"}
        self.state1.box = {}

        # Declare operators and methods.
        declare_operators(move_to, cross_door)
        declare_operators(move_to, cross_door, open_door,
                          close_door, pickup, drop)
        declare_methods("navigate", navigate)
        declare_methods("fetch", fetch)
        declare_methods("transport", transport)
    """
    initializaion
    """

    def run(self):
        """
        Initiates the main application loop.
        """
        self.view.mainloop()

    def setup_initial_gui_state(self):
        """
        Sets up the initial state of the GUI by creating main frames, dropdowns, and buttons.
        """
        self.view.main_frames()
        self.view.interactions()

    def solve(self):
        """
        Solves the current problem based on the GUI inputs and selected task.
        Clears the solution box, sets up the state, and executes the planning algorithm.
        """
        self.view.solution_box.delete("1.0", "end")
        state1 = State("state")
        state1.pos = self.view.start_pos_choice.get()
        state1.door = self.state1.door
        state1.holding = False
        state1.box = {"box1": self.view.box_pos_choice.get()} if self.view.box_pos_choice.get() else {}
        end_loc = self.view.end_pos_choice.get()

        if state1.pos == "":
            self.view.solution_box.insert("end", "No starting point selected")
        if not state1.box:
            plan = pyhop(state1, [('navigate', end_loc)], verbose=3)
            self.view.solution_box.insert("end", f"Task: \"navigate\", {end_loc}\n")
        elif state1.box["box1"] == end_loc:
            plan = pyhop(state1, [('fetch', "box1")], verbose=3)
            self.view.solution_box.insert("end", f"Task: \"fetch\", \"box1\"\n")
        else:
            plan = pyhop(state1, [('transport', "box1", end_loc)], verbose=3)
            self.view.solution_box.insert("end", f"Task: \"transport\", {end_loc}, \"box1\"\n")
        if plan:
            self.view.after(
                500, lambda: self.animate_plan(plan))
        else:
            self.view.solution_box.insert("end", "No plan found.\n")

    def animate_plan(self, plan, step_index=0, holding=False):
        """
        Animates the execution of a plan step by step.

        Args:
            plan (list): The list of actions constituting the plan.
            step_index (int): The current step of the plan to execute.
            holding (bool): Indicating whether the robot is holding the box.
        """
        if step_index >= len(plan):
            self.view.solution_box.insert("end", f"SUCCESS\n")
            return

        action, *args = plan[step_index]

        action_operators = {"move_to": self.move_to,
                            "cross_door": self.cross_door,
                            "open_door": self.open_door,
                            "close_door": self.close_door,
                            "pickup": self.pickup,
                            "drop": self.drop}

        if action in action_operators:
            result = action_operators[action](*args, holding=holding)
            if action == "pickup" or action == "drop":
                holding = result
        self.view.solution_box.see("end")
        self.view.after(500, lambda: self.animate_plan(
            plan, step_index+1, holding))

    def move_to(self, loc, holding):
        """
        Moves the robot to the specified location.

        Args:
            loc (str): The target location to move to.
            holding (bool): Indicating whether the robot is holding the box.
        """
        self.view.start_pos_choice.set(loc)
        if holding:
            self.view.box_pos_choice.set(loc)
            self.move_box()
        self.move_robot()
        self.view.solution_box.insert("end", f"Moving to: {loc}\n")

    def cross_door(self, door, loc, holding):
        """
        Moves the robot through a door to a new location.

        Args:
            door (str): The door to cross.
            loc (str): The target location after crossing the door.
            holding (bool): Indicating whether the robot is holding the box.
        """
        self.view.start_pos_choice.set(loc)
        if holding:
            self.view.box_pos_choice.set(loc)
            self.move_box()
        self.move_robot()
        self.view.solution_box.insert(
            "end", f"Crossing door: {door} to {loc}\n")

    def open_door(self, door, holding):
        """
        Opens the specified door.

        Args:
            door (str): The door to open.
            holding (bool): Indicating whether the robot is holding the box (unused here but kept for consistency).
        """
        self.view.toggle_door_color(door)
        self.view.solution_box.insert("end", f"Opening door: {door}\n")

    def close_door(self, door, holding):
        """
        Closes the specified door.

        Args:
            door (str): The door to close.
            holding (bool): Indicating whether the robot is holding the box (unused here but kept for consistency).
        """
        self.view.toggle_door_color(door)
        self.view.solution_box.insert("end", f"Closing door: {door}\n")

    def pickup(self, box, holding):
        """
        Picks up the specified box.

        Args:
            box (str): The box to pick up.
            holding (bool): Indicating whether the robot is holding the box. (unused here but kept for consistency).

        Returns:
            True to indicate that the robot is now holding the box.
        """
        self.view.solution_box.insert("end", f"Picking up: {box}\n")
        return True

    def drop(self, box, holding):
        """
        Drops the specified box at the robot's current location.

        Args:
            box (str): The box to drop.
            holding (bool): Indicating whether the robot is holding the box.

        Returns:
            False to indicate that the robot is no longer holding the box.
        """
        current_coords = self.view.canvas.coords(self.view.box_item)
        pos = self.view.start_pos_choice.get()
        x, y = self.view.points_dict[pos]
        dx = x - (current_coords[0] + current_coords[2]) / 2
        dy = y - (current_coords[1] + current_coords[3]) / 2 - 80
        self.view.canvas.move(self.view.box_item, dx, dy)
        self.view.solution_box.insert("end", f"Dropping: {box}\n")
        return False

    def reset(self):
        """
        Resets the GUI to its initial state.
        """
        self.setup_initial_gui_state()

    def move_robot(self, event=None):
        """
        Moves the robot to the selected start position.
        """
        current_coords = self.view.canvas.coords(self.view.roby)
        pos = self.view.start_pos_choice.get()
        x, y = self.view.points_dict[pos]
        dx = x - (current_coords[0] + current_coords[2]) / 2
        dy = y - (current_coords[1] + current_coords[3]) / 2
        self.view.canvas.move(self.view.roby, dx, dy)
        self.view.canvas.tag_raise(self.view.point_text_items[pos])

    def move_box(self,event=None):
        """
        Moves the box to the selected position.
        """
        if self.view.box_item is not None:
            self.view.canvas.delete(self.view.box_item)
        self.view.box_item = self.view.box()
        current_coords = self.view.canvas.coords(self.view.box_item)
        pos = self.view.box_pos_choice.get()
        x, y = self.view.points_dict[pos]
        dx = x - (current_coords[0] + current_coords[2]) / 2
        dy = y - (current_coords[1] + current_coords[3]) / 2
        self.view.canvas.move(self.view.box_item, dx, dy)
        self.view.canvas.tag_raise(self.view.point_text_items[pos])

    def random_pos(self):
        """
        Returns a random position key from the points dictionary.
        """
        return random.choice(list(self.view.points_dict.keys()))
    
    def test_methods(self, type):
        """
        Tests various methods (navigate, fetch, transport) with randomly selected start, end, and box positions.

        Args:
            type (str): The type of task to test ("navigate", "fetch", "transport").
            event: Optional event parameter for event-driven calls.
        """
        def random_pos():
            return random.choice(list(self.view.points_dict.keys()))
        random_start = random_pos()
        random_end = random_pos()
        random_box = random_pos()
        
        state1 = State("state")
        state1.pos = random_start
        state1.door = self.state1.door
        state1.box = {"box1":random_end}
        state1.holding = False     
        self.view.start_pos_choice.set(state1.pos)
        self.view.end_pos_choice.set(random_end)
        self.view.set_end_pos()
        self.move_robot()
        if type == "navigate":
            plan = pyhop(state1, [('navigate', random_end)], verbose=3)
            self.view.solution_box.insert("end", f"Task: \"navigate\", {random_end}\n")
        elif type == "fetch":
            self.view.box_pos_choice.set(random_end)
            self.move_box()
            plan = pyhop(state1, [('fetch', "box1")], verbose=3)
            self.view.solution_box.insert("end", f"Task: \"fetch\", \"box1\"\n") 
        elif type == "transport":
            self.view.box_pos_choice.set(random_box)
            state1.box = {"box1":random_box}
            self.move_box()
            plan = pyhop(state1, [('transport', "box1", random_end)], verbose=3)
            self.view.solution_box.insert("end", f"Task:    (\"transport\", \"box1\", {random_end})\n")
        
        if plan:
            self.view.after(
                500, lambda: self.animate_plan(plan))
        else:
            self.view.solution_box.insert("end", "No plan found.\n")
