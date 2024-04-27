import pygame
from Cell import cell

class board:
    # initializes the attributes of the board, such as its width, height,
    # the Pygame window (screen), and the difficulty level chosen by the user
    def __init__(self, width, height, screen, difficulty, boardvalues):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.grid = [[cell(boardvalues[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None

    def draw(self):
        # draws the Sudoku grid on the Pygame window. It draws the grid lines to
        # delineate the 3x3 boxes and then draws every cell on the board
        cell_size = self.width // 9
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, i * cell_size),
                                 (self.width, i * cell_size),
                                 4)

                pygame.draw.line(self.screen,
                                 (0, 0, 0),
                                 (i * cell_size, 0),
                                 (i * cell_size, self.height),
                                 4)
            else:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, i * cell_size),
                                 (self.width, i * cell_size),
                                 2)
                pygame.draw.line(self.screen,
                                 (0, 0, 0),
                                 (i * cell_size, 0),
                                 (i * cell_size, self.height),
                                 2)

        # Draw cells
        for row in range(9):
            for col in range(9):
                self.grid[row][col].draw()

    def select(self, row, col):
        # marks the cell at the given (row, col) position as the currently selected cell.
        # This allows the user to edit its value or sketched value
        self.selected_cell = (row, col)

    def click(self, x, y):
        # given the coordinates (x, y) of a click event on the Pygame window,
        # this function returns the row and column indices of the cell that was clicked on
        # and if the click event is outside the board area then it'll returns None
        cell_size = self.width // 9
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // cell_size
            col = x // cell_size
            return row, col
        else:
            return None

    def clear(self):
        # Clears the value of the currently selected cell.
        # Note that the user can only remove the cell values and sketched values
        # that they have filled themselves
        if self.selected_cell:
            row, col = self.selected_cell
            if not self.grid[row][col].is_original():
                self.grid[row][col].clear()

    def sketch(self, value):
        # sets the sketched value of the currently selected cell equal to
        # the user-entered value but displays at the top-left corner of the cell
        if self.selected_cell:
            row, col = self.selected_cell
            if not self.grid[row][col].is_original():
                self.grid[row][col].set_sketched_value(value)

    def place_number(self, value):
        # sets the value of the currently selected cell equal to
        # the user-entered value. (method will be called when the user presses the Enter key)
        if self.selected_cell:
            row, col = self.selected_cell
            # if not self.grid[row][col].is_original():
            self.grid[row][col].set_cell_value(value)

    def reset_to_original(self):
        # resets all cells in the board to their original values.
        # (when a cell is empty, it will set it to 0)
        for row in range(9):
            for col in range(9):
                if not self.grid[row][col].is_original():
                    self.grid[row][col].reset()

    def is_full(self):
        # returns a Boolean value indicating whether the board is full or not.
        # If any cell still has a value of 0, it returns False; otherwise, it returns True.
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].get_value() == 0:
                    return False
        return True

    def update_board(self):
        # updates the underlying 2D board with the values in all cells
        for row in range(9):
            for col in range(9):
                self.grid[row][col].update_value()

    def find_empty(self):
        # finds an empty cell (a cell with a value of 0) on the board and returns
        # its row and column indices as a tuple (row, col).
        # If no empty cell is found, it returns None.
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].get_value() == 0:
                    return row, col
        return None

    def check_board(self):
        # Checks whether the Sudoku board is solved correctly.
        # Checks for duplicate numbers in rows, columns, and 3x3 boxes.
        # If the board is solved correctly, it returns True; otherwise, it returns False
        for row in range(9):
            nums = set()
            for col in range(9):
                value = self.grid[row][col].get_value()
                if value != 0:
                    if value in nums:
                        return False
                    else:
                        nums.add(value)

        # Check columns
        for col in range(9):
            nums = set()
            for row in range(9):
                value = self.grid[row][col].get_value()
                if value != 0:
                    if value in nums:
                        return False
                    else:
                        nums.add(value)

        # Check 3x3 boxes
        for i in range(3):
            for j in range(3):
                nums = set()
                for row in range(3 * i, 3 * (i + 1)):
                    for col in range(3 * j, 3 * (j + 1)):
                        value = self.grid[row][col].get_value()
                        if value != 0:
                            if value in nums:
                                return False
                            else:
                                nums.add(value)

        return True