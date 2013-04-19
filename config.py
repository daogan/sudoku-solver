'''
  config settings for GUI sudoku solver.
'''

# window properties
CAPTION = 'Sudoku Solver'
RESOLUTION = (1280, 820)
FRAME_RATE = 30

# board layout
BOARD_Y = 100

# sudoku size
BOX_SIZE = 3
GRID_SIZE = BOX_SIZE * BOX_SIZE
CHAR = '1'

B_SIZE = {1: 540, 2: 540, 3: 540, 4: 560, 5: 600, 6: 612}
# BOARD_SIZE % GRID_SIZE == 0
BOARD_SIZE = B_SIZE[BOX_SIZE]

# color settings
COLOR_BACKGROUND   = 'white'
COLOR_CELL_DEFAULT = 0xEFF3EE00
COLOR_CELL_FILLED  = 'white'
COLOR_THICK_LINE   = 'grey30'
COLOR_THIN_LINE    = 'grey50' 
COLOR_MOUSE_OVER   = 'yellow'
COLOR_GRID_TEXT    = 'black'
COLOR_SOLVE_TEXT   = 'darkgreen'
COLOR_HELP_TEXT    = 'red'
