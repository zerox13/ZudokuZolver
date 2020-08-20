import numpy as np
import random

solutionNr = 1
sudoku = np.array([[8, 1, 0, 0, 3, 0, 0, 2, 7],
                   [0, 6, 2, 0, 5, 0, 0, 9, 0],
                   [0, 7, 0, 0, 0, 0, 0, 0, 0],
                   [0, 9, 0, 6, 0, 0, 1, 0, 0],
                   [1, 0, 0, 0, 2, 0, 0, 0, 4],
                   [0, 0, 8, 0, 0, 5, 0, 7, 0],
                   [0, 0, 0, 0, 0, 0, 0, 8, 0],
                   [0, 2, 0, 0, 1, 0, 7, 5, 0],
                   [3, 8, 0, 0, 7, 0, 0, 0, 0]])



def isPossible(x, y, n):
    if n in sudoku[x] or n in sudoku[:, y]:
        return False
    else:
        subGridX = (x//3)*3
        subGridY = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                if sudoku[subGridX + i][subGridY+j] == n:
                    return False
        return True


def solve():
    global sudoku
    global solutionNr
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if isPossible(i, j, n):
                        sudoku[i][j] = n
                        solve()
                        sudoku[i][j] = 0
                return False
    print("Solution nr " + repr(solutionNr) + ":")
    print(sudoku)
    print()
    print()
    solutionNr = solutionNr +1



solve()
print("Wooohooo!!! \n There was totally " + repr(solutionNr-1)+ " solutions\n")