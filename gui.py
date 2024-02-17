from customtkinter import *
from tkinter import *
from pyhop.pyhop import *
from PIL import Image, ImageTk

set_appearance_mode("Dark")
set_default_color_theme("dark-blue")

class Lab_4GUI(CTk):
    def __init__(self, controller):
        """
        Initializes the GUI for the lab application.

        Args:
            controller (class type): The controller that manages interactions between the GUI and the application logic.
        """
        super().__init__()
        self.controller = controller
        self.geometry("1600x1000")

        self.point_items = {}
        self.point_text_items = {}

        self.door_items = {}
        self.room_items = {}
        self.box_item = None

        self.points_dict = {
            "p1": (125, 125),
            "p2": (375, 125),
            "p3": (535, 255),
            "p4": (665, 255),
            "p5": (825, 125),
            "p6": (1025, 125),
            "p7": (355, 425),
            "p8": (355, 575),
            "p9": (125, 825),
            "p10": (375, 825),
            "p11": (835, 745),
            "p12": (965, 745),
            "p13": (675, 825),
            "p14": (1125, 825),
            "p15": (755, 425),
            "p16": (755, 575),
        }
        
        self.roby_png = Image.open('img/robot.png')
        self.roby_png = self.roby_png.resize((100, 100))
        self.roby_display = ImageTk.PhotoImage(self.roby_png)
        
        self.box_png = Image.open('img/Box.png')
        self.box_png = self.box_png.resize((80, 60))
        self.box_display = ImageTk.PhotoImage(self.box_png)

    def main_frames(self):
        """
        Sets up the main frames and canvas elements of the GUI, including rooms, doors, and points.
        """
        self.canvas = Canvas(self, bg="grey93", width=1200, height=1000, bd=0)
        self.canvas.place(x=0, y=0)

        # Rooms - 1,2,3,4
        self.room_items["room1"] = self.canvas.create_rectangle(0, 0, 600, 500, outline="black", fill="", width=5)
        self.room_items["room2"] = self.canvas.create_rectangle(600, 0, 1200, 500, outline="black", fill="", width=5)
        self.room_items["room3"] = self.canvas.create_rectangle(0, 500, 600, 1000, outline="black", fill="", width=5)
        self.room_items["room4"] = self.canvas.create_rectangle(600, 500, 900, 1000, outline="black", fill="", width=5)
        self.room_items["room5"] = self.canvas.create_rectangle(900, 500, 1200, 1000, outline="black", fill="", width=5)

        # Doors - 1,2,3,4
        self.door_items["door1"] = self.canvas.create_rectangle(580, 200, 620, 300, outline="black", fill="grey70", width=2)
        self.door_items["door2"] = self.canvas.create_rectangle(300, 480, 400, 520, outline="black", fill="grey70", width=1)
        self.door_items["door3"] = self.canvas.create_rectangle(700, 480, 800, 520, outline="black", fill="grey70", width=1)
        self.door_items["door4"] = self.canvas.create_rectangle(880, 700, 920, 800, outline="black", fill="grey70", width=1)

        # Room 1 positions
        self.point_items["p1"] = self.canvas.create_oval(100, 100, 150, 150, outline="black", fill="grey70", width=3)
        self.point_items["p2"] = self.canvas.create_oval(350, 100, 400, 150, outline="black", fill="grey70", width=3)
        self.point_items["p3"] = self.canvas.create_oval(510, 230, 560, 280, outline="black", fill="grey70", width=3)
        self.point_items["p7"] = self.canvas.create_oval(330, 400, 380, 450, outline="black", fill="grey70", width=3)
        self.point_text_items["p1"] = self.canvas.create_text(125, 125, font=(None, 20), text="p1")
        self.point_text_items["p2"] = self.canvas.create_text(375, 125, font=(None, 20), text="p2")
        self.point_text_items["p3"] = self.canvas.create_text(535, 255, font=(None, 20), text="p3")
        self.point_text_items["p7"] = self.canvas.create_text(355, 425, font=(None, 20), text="p7")
        self.room1_label = self.canvas.create_text(300,250, font=(None, 20), text="room1")

        # Room 2 positions
        self.point_items["p4"] = self.canvas.create_oval(640, 230, 690, 280, outline="black", fill="grey70", width=3)
        self.point_items["p5"] = self.canvas.create_oval(800, 100, 850, 150, outline="black", fill="grey70", width=3)
        self.point_items["p6"] = self.canvas.create_oval(1000, 100, 1050, 150, outline="black", fill="grey70", width=3)
        self.point_items["p15"] = self.canvas.create_oval(730, 400, 780, 450, outline="black", fill="grey70", width=3)
        self.point_text_items["p4"] = self.canvas.create_text(665, 255, font=(None, 20), text="p4")
        self.point_text_items["p5"] = self.canvas.create_text(825, 125, font=(None, 20), text="p5")
        self.point_text_items["p6"] = self.canvas.create_text(1025, 125, font=(None, 20), text="p6")
        self.point_text_items["p15"] = self.canvas.create_text(755, 425, font=(None, 20), text="p15")
        self.room2_label = self.canvas.create_text(900,250, font=(None, 20), text="room2")

        # Room 3 positions
        self.point_items["p8"] = self.canvas.create_oval(330, 550, 380, 600, outline="black", fill="grey70", width=3)
        self.point_items["p9"] = self.canvas.create_oval(100, 800, 150, 850, outline="black", fill="grey70", width=3)
        self.point_items["p10"] = self.canvas.create_oval(350, 800, 400, 850, outline="black", fill="grey70", width=3)
        self.point_text_items["p8"] = self.canvas.create_text(355, 575, font=(None, 20), text="p8")
        self.point_text_items["p9"] = self.canvas.create_text(125, 825, font=(None, 20), text="p9")
        self.point_text_items["p10"] = self.canvas.create_text(375, 825, font=(None, 20), text="p10")
        self.room3_label = self.canvas.create_text(300,750, font=(None, 20), text="room3")

        # Room 4 positions
        self.point_items["p11"] = self.canvas.create_oval(810, 720, 860, 770, outline="black", fill="grey70", width=3)
        self.point_items["p13"] = self.canvas.create_oval(650, 800, 700, 850, outline="black", fill="grey70", width=3)
        self.point_items["p16"] = self.canvas.create_oval(730, 550, 780, 600, outline="black", fill="grey70", width=3)
        self.point_text_items["p11"] = self.canvas.create_text(835, 745, font=(None, 20), text="p11")        
        self.point_text_items["p13"] = self.canvas.create_text(675, 825, font=(None, 20), text="p13")
        self.point_text_items["p16"] = self.canvas.create_text(755, 575, font=(None, 20), text="p16")
        self.room4_label = self.canvas.create_text(750,750, font=(None, 20), text="room4")
        
        # Room 5 positions
        self.point_items["p12"] = self.canvas.create_oval(940, 720, 990, 770, outline="black", fill="grey70", width=3)
        self.point_items["p14"] = self.canvas.create_oval(1100, 800, 1150, 850, outline="black", fill="grey70", width=3)
        self.point_text_items["p12"] = self.canvas.create_text(965, 745, font=(None, 20), text="p12")
        self.point_text_items["p14"] = self.canvas.create_text(1125, 825, font=(None, 20), text="p14")
        self.room5_label = self.canvas.create_text(1050,750, font=(None, 20), text="room5")

        # Setting up toggles for Doors (Open: White, Closed:Black)
        self.canvas.tag_bind(self.door_items["door1"], "<Button-1>", lambda e: self.toggle_door_color("door1"))
        self.canvas.tag_bind(self.door_items["door2"], "<Button-1>", lambda e: self.toggle_door_color("door2"))
        self.canvas.tag_bind(self.door_items["door3"], "<Button-1>", lambda e: self.toggle_door_color("door3"))
        self.canvas.tag_bind(self.door_items["door4"], "<Button-1>", lambda e: self.toggle_door_color("door4"))

        # Robot representation
        # self.roby = self.canvas.create_rectangle(90, 90, 160, 160, outline="black", fill="blue", width=3)
        self.roby = self.canvas.create_image(300,300, image=self.roby_display)

        self.right_frame = CTkFrame(self, height=1000, width=400)
        self.right_frame.place(x=1200, y=0)
        self.info = CTkLabel(self.right_frame, font=(None, 16), text="HTN lab 4\nChoose a starting point and an end point for the robot(blue) to navigate. You can click on the doors to open or close them (white=open, black=closed).\n\n You can also include a box(orange). If box is included, the robot will first fetch the box, then navigate to the end point and drop it.\n", wraplength=400 - 10)
        self.info.pack()


    def interactions(self):
        """
        Initializes the interactive components of the GUI, such as dropdowns and buttons for selecting points and executing actions.
        """
        self.start_pos_choice = StringVar(value="")
        self.end_pos_choice = StringVar(value="")
        self.box_pos_choice = StringVar(value="")

        self.solve = CTkButton(self.right_frame, text="SOLVE", command=self.controller.solve).pack(pady=5)
        self.reset = CTkButton(self.right_frame, text="RESET", command=self.controller.reset).pack(pady=5)
        self.solution_box = CTkTextbox(self.right_frame, width=400, height=400, font=(None, 16))
        self.solution_box.pack()
        self.test_navigate = CTkButton(self.right_frame, text="Test Navigate", command=lambda : self.controller.test_methods("navigate")).pack(pady=5)
        self.test_fetch = CTkButton(self.right_frame, text="Test Fetch", command=lambda : self.controller.test_methods("fetch")).pack(pady=5)
        self.test_transport = CTkButton(self.right_frame, text="Test Transport", command=lambda : self.controller.test_methods("transport")).pack(pady=5)

        self.start_pos_text = CTkLabel(self.right_frame, text="Set starting point").pack()
        self.start_pos = CTkComboBox(self.right_frame, variable=self.start_pos_choice, width=75, values=list(self.points_dict.keys()), command=self.controller.move_robot).pack()
        self.end_pos_text = CTkLabel(self.right_frame, text="Set end point").pack()
        self.end_pos = CTkComboBox(self.right_frame, variable=self.end_pos_choice, width=75, values=list(self.points_dict.keys()), command=self.set_end_pos).pack()
        self.box_pos_text = CTkLabel(self.right_frame, text="Set box point").pack()
        self.box_pos = CTkComboBox(self.right_frame, variable=self.box_pos_choice, width=75, values=list(self.points_dict.keys()), command=self.controller.move_box).pack()
            

    def box(self):
        """
        Creates and returns a graphical representation of a box on the canvas.

        Returns:
            The canvas item identifier for the created box.
        """
        return self.canvas.create_image(300,300, image=self.box_display)

    def set_end_pos(self, event=None):
        """
        Highlights the selected end position on the canvas.

        Args:
            event: Optional event parameter for event-driven calls. Defaults to None.
        """
        pos = self.end_pos_choice.get()
        color_point = self.point_items[pos]
        for key in list(self.point_items.keys()):
            point = self.point_items[key]
            self.canvas.itemconfig(point, fill="grey70")
        self.canvas.itemconfig(color_point, fill="red")

    def toggle_door_color(self, door_id):
        """
        Toggles the color of a door on the canvas to indicate its open or closed state.

        Args:
            door_id (canvas.item): The identifier for the door whose color should be toggled.
        """
        current_color = self.canvas.itemcget(self.door_items[door_id], "fill")
        new_color = "black" if current_color != "black" else "grey70"
        self.canvas.itemconfig(self.door_items[door_id], fill=new_color)
        if self.controller.state1.door[door_id] == "closed":
            self.controller.state1.door[door_id] = "open"
        else:
            self.controller.state1.door[door_id] = "closed"