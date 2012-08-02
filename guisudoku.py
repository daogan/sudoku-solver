#!/usr/bin/env python

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

# jun 01, 2012

from __future__ import division

import pygame
from pygame.locals import *
from config import *
import sudokusolver

__all__ = ['SudokuSolverGUI']

# status a cell may have
S_BLANCK    = 0
S_FILLED    = 1
S_MOUSEOVER = 2
S_SOLVED    = 4

class Cell(pygame.Rect):
    
    def __init__(self, *arg, **args):
        pygame.Rect.__init__(self, *arg, **args)
        self.char = None
        self.status = S_BLANCK
        
class SudokuSolverGUI(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('FreeSans', 
                BOARD_SIZE // GRID_SIZE * 2 // 3, True)

        self.board_pos = ((RESOLUTION[0] - BOARD_SIZE) // 2, BOARD_Y)
        self.cell_size = BOARD_SIZE // GRID_SIZE

        cell_xs = [x * self.cell_size + self.board_pos[0]
                for x in xrange(GRID_SIZE + 1)]
        cell_ys = [y * self.cell_size + self.board_pos[1] 
                for y in xrange(GRID_SIZE + 1)]

        vertical_lines_top = [(x, self.board_pos[1]) for x in cell_xs]
        vertical_lines_bottom = [(x, self.board_pos[1] + BOARD_SIZE)
                for x in cell_xs]
        horizontal_lines_left = [(self.board_pos[0], y) for y in cell_ys]
        horizontal_lines_right = [(self.board_pos[0] + BOARD_SIZE, y)
                for y in cell_ys]

        self.vertical_lines = zip(vertical_lines_top, 
                vertical_lines_bottom)
        self.horizontal_lines = zip(horizontal_lines_left, 
                horizontal_lines_right)

        self.cells = [Cell(cell_xs[i], cell_ys[j], self.cell_size, 
            self.cell_size) for j in xrange(GRID_SIZE) 
            for i in xrange(GRID_SIZE)]
        self.selected_cell = None
        self.reset_cells()

    def reset_cells(self):
        for cell in self.cells:
            cell.char = None
            cell.status = S_BLANCK

    def run(self):

        self.screen.fill(Color(COLOR_BACKGROUND))
        self.draw_help_text()
        
        while True:
            self.clock.tick(FRAME_RATE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse(event)
                elif event.type == pygame.KEYDOWN:
                    self.handle_keyboard(event)

            self.draw_cells()
            self.draw_lines()
            pygame.display.flip()

    def draw_lines(self):
        
        # draw horizontal lines
        for i, (start_pos, end_pos) in enumerate(self.horizontal_lines):
            # draw thick lines
            if i % BOX_SIZE == 0:
                pygame.draw.line(self.screen, Color(COLOR_THICK_LINE), 
                        start_pos, end_pos, 3)
            # draw thin lines
            else:
                pygame.draw.line(self.screen, Color(COLOR_THIN_LINE), 
                        start_pos, end_pos, 1)

        # draw vertical lines
        for i, (start_pos, end_pos) in enumerate(self.vertical_lines):
            # draw thick lines
            if i % BOX_SIZE == 0:
                pygame.draw.line(self.screen, Color(COLOR_THICK_LINE), 
                        start_pos, end_pos, 3)
            # draw thin lines
            else:
                pygame.draw.line(self.screen, Color(COLOR_THIN_LINE), 
                        start_pos, end_pos, 1)

    def draw_cells(self):
        for cell in self.cells:
            if cell.status & S_MOUSEOVER:
                pygame.draw.rect(self.screen, Color(COLOR_MOUSE_OVER), cell)
            elif cell.status & S_FILLED:
                pygame.draw.rect(self.screen, Color(COLOR_CELL_FILLED), cell)
            else:
                pygame.draw.rect(self.screen, Color(COLOR_CELL_DEFAULT), cell)
            if cell.status & S_FILLED:
                text = self.font.render(cell.char, True, Color(COLOR_GRID_TEXT))
                x = cell.center[0] - text.get_width() // 2
                y = cell.center[1] - text.get_height() // 2
                self.screen.blit(text, (x, y))
            elif cell.status & S_SOLVED:
                text = self.font.render(cell.char, True, Color(COLOR_SOLVE_TEXT))
                x = cell.center[0] - text.get_width() // 2
                y = cell.center[1] - text.get_height() // 2
                self.screen.blit(text, (x, y))

    def draw_help_text(self):

        title = 'Sudoku Solver'
        help_text = ['mouse hover to select cell', 
                'number <1~9> or part of <a~z> to set cell\'s value', 
                '<space> to start to solve', 
                '<r> to reset and <q> to quit']

        myfont = pygame.font.SysFont('Purisa', 20, True)
        text = myfont.render(title, 1, (250, 150, 0))
        self.screen.blit(text, (560, 10))

        myfont = pygame.font.SysFont('Dejavu Sans Mono', 10)
        y = 10
        for line in help_text:
            text = myfont.render(line, True, Color(COLOR_HELP_TEXT))
            self.screen.blit(text, (25, y))
            y += 10
        
        pass

    def handle_mouse(self, event):
        
        if event.type == pygame.MOUSEMOTION:
            for cell in self.cells:
                # set each cell's status to be (not S_MOUSEOVER)
                cell.status &= ~S_MOUSEOVER
                # only the one under the mouse is S_MOUSEOVER
                if cell.collidepoint(event.pos):
                    cell.status |= S_MOUSEOVER
                    # mark the selected cell
                    self.selected_cell = cell

    def handle_keyboard(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_r:
                print 'reseting grid...'
                self.reset_cells()
            # reset the status of a selected cell (not filled and blank)
            elif event.key == pygame.K_0:
                self.selected_cell.status |= S_BLANCK
                self.selected_cell.status &= ~S_FILLED
                self.selected_cell.char = None
            # set the status of the selected cell to be filled
            elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                if CHAR == 'A':
                    return 
                self.selected_cell.status |= S_FILLED
                self.selected_cell.char = chr(ord(CHAR) + event.key - K_1)
            elif event.key >= pygame.K_a and event.key < K_a + GRID_SIZE:
                if CHAR == '0':
                    return
                self.selected_cell.status |= S_FILLED
                self.selected_cell.char = chr(event.key - 32)
            elif event.key == pygame.K_SPACE:
                self.sudoku_solve()

    def sudoku_solve(self):

        sudoku = []
        solved = []

        for cell in self.cells:
            if cell.status & S_FILLED:
                sudoku.append(ord(cell.char) - ord(CHAR))
            else:
                sudoku.append(-1)

        print sudoku
        ss = sudokusolver.SudokuSolver(sudoku)
        for i in xrange(len(ss.answer)):
            solved.append(chr(ss.answer[i] + ord(CHAR)))
        
        print solved
        self.display_answer(solved)

    def display_answer(self, answer):

        i = 0
        for cell in self.cells:
            if not (cell.status & S_FILLED):
                char = answer[i]
                cell.char = char
                # mark the status is solved
                cell.status |= S_SOLVED
            i += 1

def main():
    sudoku = SudokuSolverGUI()
    sudoku.run()

if __name__ == '__main__':
    main()
