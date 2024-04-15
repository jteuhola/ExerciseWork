# Circuit Board Assembly Machine
# with graphical interface
# Joonas Teuhola & Oscar Salin 2024


import math


class CircuitBoard:
    def __init__(self, width: int, height: int, ID: int):
        self.w = width
        self.h = height
        self.ID = ID
        self.components = []

    def add_component(self, new_c):
        # Check if a new component can be added to a board.

        # new_c = new component
        # check if component fits in the board:
        if (new_c.y + new_c.h - 1 <= self.h) and (new_c.x + new_c.h - 1 <= self.w):
            # check if component overlaps with another component:
            can_add = True
            for c in self.components:
                if not ((c.x > (new_c.x + new_c.w-1)) or (new_c.x > c.x + c.w-1)):
                    if not ((c.y > (new_c.y + new_c.h-1)) or (new_c.y > c.y + c.h-1)):
                        # if it overlaps the don't add the new component
                        can_add = False
                        break

            if can_add:
                # Add:
                self.components.append(new_c)
            else:
                # "Error message":
                print(red)
                print(
                    f"Didn't fit: Component ID: {new_c.ID}, (x, y) = ({new_c.x}, {new_c.y}), Board ID: {self.ID}")
                print(white)


class Component:
    def __init__(self, x: int, y: int, ID: int, board_id: int):
        self.x = x
        self.y = y
        self.instanceID = ID
        self.board_ID = board_id    # which board does the component belong to


# Different component types, inherit from class Component:


class Resistor(Component):
    def __init__(self, x: int, y: int, ID: int, board_id: int):
        super().__init__(x, y, ID, board_id)
        self.w = 1
        self.h = 1
        self.ID = '1'


class LogicChip(Component):
    # for British: logic crisp
    def __init__(self, x: int, y: int, ID: int, board_id: int):
        super().__init__(x, y, ID, board_id)
        self.w = 5
        self.h = 2
        self.ID = '2'


class LEDLight(Component):
    def __init__(self, x: int, y: int, ID: int, board_id: int):
        super().__init__(x, y, ID, board_id)
        self.w = 2
        self.h = 2
        self.ID = '3'


class FluxCapacitor(Component):
    def __init__(self, x: int, y: int, ID: int, board_id: int):
        super().__init__(x, y, ID, board_id)
        self.w = 4
        self.h = 4
        self.ID = '4'


def draw_board(board):
    # Draw a circuit board.
    # Goes through every (x, y) coordinate and checks if that spot
    # has a component. If yes, the "draw" the component by writing the ID number.
    # Loop flow:
    # - add output to row_render
    # - add row_render to board_render
    # - draw board_render
    print(yellow)
    print(f'*** Circuit Board ID: {board.ID} ***')
    print(white)

    board_render = []   # initiate list
    for row in range(board.h):  # Y-value
        row_render = str()  # initiate string for every row
        for col in range(board.w):  # X-value
            output = '.'    # default = empty space

            for c in board.components:
                # check if current (x, y) are in range of a component:
                if (c.x <= col < c.x + c.w) and (c.y <= row < c.y + c.h):
                    output = c.ID   # change default output value to ID number

            # Add output to current row
            row_render += output

        # Finally, add row to whole board.
        board_render.append(row_render)

    # print horizontal row of numbers:
    # start with tens:
    print("    ", end="")  # offset
    for i in range(math.floor(board.w / 10) + 1):
        print(i, end="                   ")
    print()  # newline

    # then print single digit numbers 0-9:
    print("    ", end="")  # offset
    counter = 0
    for i in range(board.w):

        if counter > 9:
            counter = 0
        print(counter, end=" ")
        counter += 1
    print()  # newline

    # Draw every row (and its line number):
    for i in range(len(board_render)):
        end_string = " "
        if i > 9:
            end_string = ""  # leave less empty space for 2-digit numbers (> 9)
        print(i, " ", end=end_string)
        print(*board_render[i])  # asterisk to print without brackets


def get_id(instance_id):
    # Get instance id for components:
    instance_id += 1
    return instance_id


def print_title():
    color = "\033[94m"
    print("##################################")
    print("# Circuit Board Assembly Machine #")
    print("##################################")


white = "\033[37m"
red = "\033[31m"
yellow = "\033[33m"

print(yellow)
print_title()
print(white)

global instance_id
instance_id = 0

boards = []
boards.append(CircuitBoard(15, 15, len(boards)))
boards.append(CircuitBoard(10, 10, len(boards)))

# values= (Type, x, y, instance id, board id)
components = [Resistor(3, 3, get_id(instance_id), 0),
              LogicChip(5, 4, get_id(instance_id), 1),  # board 1
              LEDLight(4, 11, get_id(instance_id), 0),
              LEDLight(12, 5, get_id(instance_id), 0),
              FluxCapacitor(8, 7, get_id(instance_id), 0),
              FluxCapacitor(6, 1, get_id(instance_id), 0),  # doesn't fit
              FluxCapacitor(7, 0, get_id(instance_id), 0),
              LogicChip(5, 13, get_id(instance_id), 0)]

for c in components:
    try:
        boards[c.board_ID].add_component(c)
    except:
        print(f"Error: No such board! ID: {c.board_ID}")

# draw circuit boards:
for b in boards:
    draw_board(b)
    print()


all_components = {
    "resistor": {
        "w": 1,
        "h": 1
    }
}
