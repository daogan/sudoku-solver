# Sudoku Solver

A sudoku solver using Knuth's Algorithm X and dancing links data structure.

![] (https://raw.github.com/daogan/sudoku-solver/master/screenshot/Screenshot-1.png)
![] (https://raw.github.com/daogan/sudoku-solver/master/screenshot/Screenshot-2.png)

Solving a sudoku can be mapped to solving an Exact Cover Problem:

 * Constraint 1: each cell must have a number filled.
 * Constraint 2: each row must contain each number exactly once.
 * Constraint 3: each column must contain each number exactly once.
 * Constraint 4: each box must contain each number exactly once.
 
 + Each has 9x9 = 81 constraints, total 81x4 = 324 constraints, use 324 columns to specify these constraints.
 + Each Sudoku cell state can be specified by [Row, Col, Value], total 9x9x9 = 729 states, use 729 rows to specify these states.
 
 
In file `config.py`, Change the value of `BOX_SIZE` to get different dimensions of the sudoku you want to solve, 
change the value of `CHAR` to set the cells' displaying characters.
 
 
## Usage

Mouse hover to select cell, press number &lt;1~9&gt; or part of &lt;a~z&gt; to set cell's value, 
press &lt;SPACE&gt; to solve the sudoku, press &lt;r&gt; to reset and &lt;q&gt; to quit.

## TODO
Load pre-defined sudokus.

## License

This content is released under the 
[MIT license](http://www.opensource.org/licenses/mit-license.php).

&copy; 2012 Daogan Ao &lt;wvvwwwvvvv@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
