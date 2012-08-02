# Sudoku Solver

A sudoku solver 

![] (https://github.com/daogan/sudoku-solver/raw/master/screenshot-1.png)
![] (https://github.com/daogan/sudoku-solver/raw/master/screenshot-2.png)

Solving a sudoku can be mapped to solving an Exact Cover Problem:

 * Constraint 1: each cell must have a number filled.
 * Constraint 2: each row must contain each number exactly once.
 * Constraint 3: each column must contain each number exactly once.
 * Constraint 4: each box must contain each number exactly once.
 
 + Each has 9x9 = 81 constraints, total 81x4 = 324 constraints, use 324 columns to specify these constraints.
 + Each Sudoku cell state can be specified by [Row, Col, Value], total 9x9x9 = 729 states, use 729 rows to specify these states.
 
 
In file `config.py`, 'Change the value of `BOX_SIZE` to get different dimensions of the sudoku you want to solve, 
change the value of `CHAR` to set the cells' representative characters.
 
 
## Usage

Mouse hover to select cell, press number &lt;1~9&gt; or part of &lt;a~z&gt; to set cell's value, 
press &lt;SPACE&gt; to solve the sudoku, press &lt;r&gt; to reset and &lt;q&gt; to quit.

## TODO
Load pre-defined sudokus.

## License

This content is released under the 
[Do What The Fuck You Want To Public License](http://sam.zoy.org/wtfpl/).

&copy; 2012 Dougam Ngou &lt;wvvwwwvvvv@gmail.com&gt;

Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO. 
