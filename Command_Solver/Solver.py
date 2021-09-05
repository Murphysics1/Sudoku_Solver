# -*- coding: utf-8 -*-
import Functions as SSF
import Puzzle as p

print("Welcome to my Sudoku Solver\n\nEnter the values of your rows")
print('Mark spaces as 0\n')
# Have User input the Puzzle
puzzle = p.puzzle()

print("\nOriginal Puzzle:")
# Print the original puzzle
SSF.view_grid(puzzle)

# Solve the Puzzle
SSF.solve(puzzle)
print('\n----------------------\n')

# Print the Solution
print("Solved Puzzle:")
SSF.view_grid(puzzle)