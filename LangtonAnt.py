# Matt Chalabian
# CS 161
# July 30, 2021
# Program that carries out the Langton Ant algorithm, and lets a user specify how many steps the ant takes.

class Ant:
    """ a class that creates ants for the Langton Ant algorithm. """
    def __init__(self, board_dimensions):
        """ makes an ant object with user-input variables """
        self._row_position = row_prompt(board_dimensions)
        self._column_position = column_prompt(board_dimensions)
        self._direction = direction_prompt()
        self._steps = steps_prompt()

    def set_row_position(self, new_row_position):
        """ sets the ant's row position """
        self._row_position = new_row_position

    def get_row_position(self):
        """ gets the ant's row position """
        return self._row_position

    def set_column_position(self, new_column_position):
        """ sets the ant's column position """
        self._column_position = new_column_position

    def get_column_position(self):
        """ gets the ant's column position """
        return self._column_position

    def set_direction(self, new_direction):
        """ sets the ant's step direction """
        self._direction = new_direction

    def get_direction(self):
        """ gets the ant's step direction """
        return self._direction

    def get_steps(self):
        """ gets the ant's step amount """
        return self._steps

    def decrement_steps(self):
        """ decrements the ant's step amount by one """
        self._steps -= 1


def create_board(dimension):
    """ creates the 2d plane for the ant """
    new_board = []
    for row_index in range(0, dimension):
        new_board.append([])
        for column_index in range(0, dimension):
            new_board[row_index].append([])
            new_board[row_index][column_index] = "_"
    return new_board


def run_simulation(ant, board):
    """ runs the function to carry out the Langton Ant algorithm """
    while ant.get_steps() > 0:
        set_new_direction(ant, board)
        tile_change(ant, board)
        walk(ant, board)
        ant.decrement_steps()
    board[ant.get_row_position()][ant.get_column_position()] = "8"


def walk(ant, board):
    """ takes a direction and moves the ant one step in that direction"""
    move = 0
    direction = ant.get_direction()
    if direction == 0 or direction == 3:
        move = -1
    if direction == 1 or direction == 2:
        move = 1
    if direction == 1 or direction == 3:
        ant_column_mod = check_bounds(ant.get_column_position() + move, board)
        ant.set_column_position(ant_column_mod)
    if direction == 0 or direction == 2:
        ant_row_mod = check_bounds(ant.get_row_position() + move, board)
        ant.set_row_position(ant_row_mod)


def tile_change(ant, board):
    """ changes the tile the ant just left """
    if board[ant.get_row_position()][ant.get_column_position()] == "_":
        board[ant.get_row_position()][ant.get_column_position()] = "#"
        return
    if board[ant.get_row_position()][ant.get_column_position()] == "#":
        board[ant.get_row_position()][ant.get_column_position()] = "_"
        return


def set_new_direction(ant, board):
    """ sets new direction based on current board tile information """
    new_direction = ant.get_direction()
    if board[ant.get_row_position()][ant.get_column_position()] == "_":
        new_direction += 1
        if new_direction > 3:
            new_direction = 0
        ant.set_direction(new_direction)
    if board[ant.get_row_position()][ant.get_column_position()] == "#":
        new_direction -= 1
        if new_direction < 0:
            new_direction = 3
        ant.set_direction(new_direction)


def check_bounds(position, board):
    """ checks movement at border and wraps ant around if it moves beyond """
    if position < 0:
        position = len(board) - 1
    if position > len(board) - 1:
        position = 0
    return position


def print_board(entered_board):
    """ prints the resulting board after the ant is done walking """
    for row_index in range(0, len(entered_board)):
        board_string = ""
        for column_index in range(0, len(entered_board)):
            board_string += entered_board[row_index][column_index]
        print(board_string)


def dimension_prompt():
    """ prompts the user for dimension of 2d area for ant to explore """
    input_dimensions = 0
    print("Welcome to Langton's ant simulation!")
    print("First, please enter a number no larger than 100 for the size of the square board:")
    while input_dimensions > 100 or input_dimensions < 1:
        input_dimensions = int(input())
        if input_dimensions > 100 or input_dimensions < 1:
            print("Not a valid entry, please try again.")
    return input_dimensions


def row_prompt(input_dimensions):
    """ prompts the user for ant's starting row position """
    input_row_position = -1
    print("Now choose the ant's starting location!")
    print("Please enter a number as the starting row number, where 0 is the first row from the top.")
    while input_row_position >= input_dimensions or input_row_position < 0:
        input_row_position = int(input())
        if input_row_position >= input_dimensions or input_row_position < 0:
            print("Not a valid entry, please try again.")
    return input_row_position


def column_prompt(input_dimensions):
    """ prompts the user for ant's starting column position """
    input_column_position = -1
    print("Now, please enter a number as the starting column number, where 0 is the first column from the left.")
    while input_column_position >= input_dimensions or input_column_position < 0:
        input_column_position = int(input())
        if input_column_position >= input_dimensions or input_column_position < 0:
            print("Not a valid entry, please try again.")
    return input_column_position


def direction_prompt():
    """ prompts the user for ant's starting direction """
    input_direction = 4
    print("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left.")
    directions = {0, 1, 2, 3}
    while input_direction not in directions:
        input_direction = int(input())
        if input_direction not in directions:
            print("Not a valid entry, please try again.")
    return input_direction


def steps_prompt():
    """ prompts the user for ant's steps it will take """
    input_steps = -1
    print("Please enter the number of steps for the simulation.")
    while input_steps < 0:
        input_steps = int(input())
        if input_steps <= 0:
            print("Not a valid entry, please try again.")
    return input_steps


def main():
    """ the main function that organizes and runs the entire program in the proper order """
    board_dimensions = dimension_prompt()
    ant = Ant(board_dimensions)
    board = create_board(board_dimensions)
    run_simulation(ant, board)
    print_board(board)


main()
