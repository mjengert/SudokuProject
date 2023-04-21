import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):  # row_length had to be moved to the end due to having a value
        self.row_length = row_length  # row_length is always 9 per instructions - Julius
        self.removed_cells = removed_cells  # removed_cells could vary depending on the difficulty level chosen
        self.board = [[0 for row in range(row_length)] for col in range(row_length)]  # makes board
        self.box_length = int(math.sqrt(row_length))  # creates box length

    '''
	Returns a 2D python list of numbers which represents the board
	Parameters: None
	Return: list[list]
    '''

    # returns board in form of 9 lists within a list
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    # prints board to the console
    def print_board(self):
        for row in range(self.row_length):
            for col in range(self.row_length):
                print(self.board[row][col], end=' ')
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''

    # checks the board in the specified row for the num
    def valid_in_row(self, row, num):
        for box in range(self.row_length):
            if self.board[row][box] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''

    # checks the board in the specified col for the num
    def valid_in_col(self, col, num):
        for box in range(self.row_length):
            if self.board[box][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    # checks the board in specified box of 3x3 for num
    def valid_in_box(self, row_start, col_start, num):
        for row in range(self.box_length):
            for col in range(self.box_length):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    # calls valid methods for row, col, and box, to determine if num is valid
    def is_valid(self, row, col, num):
        row_valid = self.valid_in_row(row, num)
        col_valid = self.valid_in_col(col, num)
        box_valid = self.valid_in_box((row - row % self.box_length), (col - col % self.box_length), num)
        if row_valid and col_valid and box_valid:
            return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    # uses specific box and generates a random value to fill all empty cells within box
    def fill_box(self, row_start, col_start):
        filling = True
        value = 0
        for row in range(self.box_length):
            for col in range(self.box_length):
                while filling:
                    value = (math.floor(random.random() * 9 + 1))
                    if self.valid_in_box(row_start, col_start, value):
                        break
                self.board[row_start + row][col_start + col] = value

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    # uses the 3 diagonal boxes and calls the fill box method at those specific rows and cols
    def fill_diagonal(self):
        for box in range(0, self.row_length, self.box_length):
            self.fill_box(box, box)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

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

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    # calls fill_diagonal and fill_remaining to first fill the diagonal values and then fill remaining values
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    # removes values from the board after board is created and filled
    # uses original removed cell value to count down until all removed cells are removed\
    # randomly iterates to find values that can be removed
    def remove_cells(self):
        count = self.removed_cells
        while count != 0:
            row = (math.floor(random.random() * 9 + 1)) - 1
            col = (math.floor(random.random() * 9 + 1)) - 1
            if self.board[row][col] != 0:
                count -= 1
                self.board[row][col] = 0
        return


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=' ')
        print()
