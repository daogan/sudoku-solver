
#          DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                Version 2, December 2004

# Copyright (C) 2012 Dougam Ngou <wvvwwwvvvv@gmail.com> 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 

#          DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

# 0. You just DO WHAT THE FUCK YOU WANT TO. 

'''
 This program is free software. It comes without any warranty, to
 the extent permitted by applicable law. You can redistribute it
 and/or modify it under the terms of the Do What The Fuck You Want
 To Public License, Version 2, as published by Sam Hocevar. See
 http://sam.zoy.org/wtfpl/COPYING for more details.
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
