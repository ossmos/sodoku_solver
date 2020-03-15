import time

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(board):
    pass
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        global counter
        counter += 1
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0


def valid(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False


    #check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False


    #check cubes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y *3, box_y + 3):
        for j in range(box_x *3, box_x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True




def print_board(board):
    for i in range(len(board)):       
        if i % 3 == 0 and i != 0:
            print ("-"*27)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col

counter = 0

#print_board(board)
solve(board)
#print("#"*20)
print_board(board)
print("amount of tries: " + str(counter))

#############################################################################

# function solve( board )
#     if the board contains no invalid cells, ie.cells that violate the rules:
#         if it is also completely filled out then
#             return true
#     for each cell in the board
#         if the cell is empty
#             for each number in {1,2,3}
#                 replace the current cell with number
#                 if solve(board) and the board is valid
#                     return true
#                 else
#                     backtrack
#         return false

#############################################################################

# from itertools import *
# from copy import copy



# def is_distinct( list ):
#     '''Auxiliary function to is_solved
#     checks if all elements in a list are distinct
#     (ignores 0s though)
#     '''
#     used = []
#     for i in list:
#         if i == 0:
#             continue
#         if i in used:
#             return False
#         used.append(i)
#     return True


# def is_valid( brd ):
#     '''Checks if a 3x3 mini-Sudoku is valid.'''
#     for i in range(3):
#         row = [brd[i][0],brd[i][1],brd[i][2]]
#         if not is_distinct(row):
#             return False
#         col = [brd[0][i],brd[1][i],brd[2][i]]
#         if not is_distinct(col):
#             return False
#     return True

# def solve( brd , empties = 9):
#     '''
#       Solves a mini-Sudoku
#       brd is the board
#       empty is the number of empty cells
#     '''

#     if empties == 0:
#         #Base case
#         return is_valid( brd )
#     for row,col in product(range(3),repeat=2):
#         #Run through every cell
#         cell = brd[row][col]
#         if cell != 0:
#             #If its not empty jump
#             continue
#         brd2 = copy( brd )
#         for test in [1,2,3]:
#             brd2[row][col] = test
#             if is_valid(brd2) and solve(brd2,empties-1):
#                 return True
#             #BackTrack
#             brd2[row][col] = 0
#     return False

# Board = [ [ 0 , 0 , 0 ],
#           [ 1 , 0 , 0 ],
#           [ 0 , 3 , 1 ] ]
# solve( Board , 9 - 3 )


# for row in Board:#Prints a solution
#     print row    






