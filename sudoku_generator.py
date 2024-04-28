import pygame
import random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(self.row_length ** 0.5)
        self.board = [[0 for j in range(9)] for i in range(9)]
        self.diagonal = False

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        for col in range(9):
            if num == self.board[row][col]:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in range(9):
            if num == self.board[row][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if num == self.board[row][col]:
                    return False
        return True

    def is_valid(self, row, col, num):
        # find col_start of box
        if 0 <= col <= 2:
            col_start = 0
        if 3 <= col <= 5:
            col_start = 3
        if 6 <= col <= 8:
            col_start = 6
        # find row_start of box
        if 0 <= row <= 2:
            row_start = 0
        if 3 <= row <= 5:
            row_start = 3
        if 6 <= row <= 8:
            row_start = 6

        if self.valid_in_box(row_start, col_start, num):
            if self.valid_in_col(col, num):
                if self.valid_in_row(row, num):
                    return True
        return False

    def fill_box(self, row_start, col_start):
        valid_nums = [i for i in range(1, 10, 1)]
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                num = valid_nums[random.randrange(0, len(valid_nums), 1)]
                self.board[row][col] = num
                valid_nums.remove(num)

    def fill_diagonal(self):
        if not self.diagonal:
            self.fill_box(0, 0)
            self.fill_box(3, 3)
            self.fill_box(6, 6)
            self.diagonal = True

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        removed = 0
        while removed < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] == 0:
                continue
            else:
                self.board[row][col] = 0
                removed += 1


class Cell:
    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketchable = False
        if self.value == 0:
            self.sketchable = True
        self.sketched_value = 0
        self.size = 50
        self.y_displacement = 1.5 * self.size
        self.x_displacement = 2 * self.size
        self.x = self.col * self.size + self.x_displacement
        self.y = self.row * self.size + self.y_displacement

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.sketched_value = value

    def draw(self):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
        font = pygame.font.SysFont("Courier New", 20)
        font.set_bold(True)

        pygame.draw.rect(self.screen, [255, 255, 255], (self.x, self.y, self.size, self.size), 0)
        centerx, centery = self.x + self.size / 2, self.y + self.size / 2
        if self.value != 0 or self.sketched_value != 0:
            if not self.sketchable:
                text_surface = font.render(str(self.value), 1, [64, 64, 64])
                text_rect = text_surface.get_rect(center=(centerx, centery))
                self.screen.blit(text_surface, text_rect)
            elif self.sketchable:
                text_surface = font.render(str(self.sketched_value), 1, [128, 128, 128])
                self.screen.blit(text_surface, (self.x + 1, self.y + 1))


class Board:
    def __init__(self, width, height, screen, difficulty):
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.sudoku = SudokuGenerator(9, self.difficulty)
        self.sudoku.fill_values()
        self.sudoku.remove_cells()
        self.original_board = [[j for j in self.sudoku.board[i]] for i in range(len(self.sudoku.board))]
        self.cells = [[Cell(self.sudoku.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.size = 50
        self.y_displacement = 1.5 * self.size
        self.x_displacement = 2 * self.size

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        for i in range(len(self.cells)):
            for cell in self.cells[i]:
                cell.draw()
        gap = self.width / 9
        for i in range(10):
            if i % 3 == 0:
                width = 4
            else:
                width = 1
            x_hor = 0 + self.x_displacement, self.width + self.x_displacement
            y_hor = i * gap + self.y_displacement
            pygame.draw.line(self.screen, (64, 64, 64), (x_hor[0], y_hor), (x_hor[1], y_hor), width)
            x_vert = i * gap + self.x_displacement
            y_vert = 0 + self.y_displacement, self.height + self.y_displacement
            pygame.draw.line(self.screen, (64, 64, 64), (x_vert, y_vert[0]), (x_vert, y_vert[1]), width)

    def select(self, row, col):
        # Marks the cell at (row,col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        row = int(row)
        col = int(col)
        self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        # If a tuple of (x,y) coordinates is within the displayed board, this function returns a tuple of the (row,col)
        # of the cell which was clicked. Otherwise, this function returns None.
        cell = self.cells[0][0]
        if cell.x_displacement <= x <= self.width + cell.x_displacement and cell.y_displacement <= y <= self.height + cell.y_displacement:

            row = int((y - cell.y_displacement) // self.size)
            col = int((x - cell.x_displacement) // self.size)
            cell = self.cells[row][col]
            return cell.row, cell.col
        else:
            return None

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        if self.selected_cell.sketched == True:
            self.selected_cell.set_sketched_value(0)
            self.selected_cell.set_cell_value(0)
            self.selected_cell = None

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed in the top left corner of the cell using the draw() function.
        cell = self.selected_cell
        cell.set_sketched_value(value)

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        cell = self.selected_cell
        cell.set_cell_value(value)
        cell.sketchable = False
        cell.set_sketched_value(0)

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        self.cells = [[Cell(self.original_board[row][col], row, col, self.screen) for col in range(9)] for row in
                      range(9)]

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for row in range(9):
            for cell in self.cells[row]:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for row in range(9):
            for col in range(9):
                self.sudoku.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.value == 0:
                    return row, col
        return None

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        for row in range(9):
            for col in range(9):
                # get the value of each column of each row
                value = self.sudoku.board[row][col]
                # check the row for validity
                for i in range(9):
                    if self.sudoku.board[row][i] == value and col != i:
                        return False

                # check the column for validity
                for i in range(9):
                    if self.sudoku.board[i][col] == value and row != i:
                        return False

                # check the box for validity
                row_start = (row // 3) * 3
                col_start = (col // 3) * 3
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if value == self.sudoku.board[i][j] and (row, col) != (i, j):
                            return False
        # if no box is marked invalid, this returns true
        return True
        

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board