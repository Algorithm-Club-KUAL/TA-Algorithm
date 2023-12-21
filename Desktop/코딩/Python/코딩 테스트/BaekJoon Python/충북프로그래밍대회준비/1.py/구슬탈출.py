import copy
#구현 알고리즘

# Define the four possible moves: tilt to the right, tilt to the left, tilt to the top, tilt to the bottom
MOVES = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Function to check if the given position is valid on the game board
def is_valid_position(position, board):
    x, y = position
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False
    if board[x][y] == '#':
        return False
    return True

# Function to perform a move on the game board and return the new state
def perform_move(board, move):
    new_board = copy.deepcopy(board)
    red_position = None
    blue_position = None
    hole_position = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                red_position = (i, j)
            elif board[i][j] == 'B':
                blue_position = (i, j)
            elif board[i][j] == 'O':
                hole_position = (i, j)
    dx, dy = move
    # Move the red marble
    new_red_position = (red_position[0] + dx, red_position[1] + dy)
    if is_valid_position(new_red_position, board):
        if new_red_position == hole_position:
            # Success! The red marble has been pulled through the hole.
            new_board[red_position[0]][red_position[1]] = '.'
            new_board[new_red_position[0]][new_red_position[1]] = 'R'
            return new_board, True
        elif new_red_position != blue_position:
            new_board[red_position[0]][red_position[1]] = '.'
            new_board[new_red_position[0]][new_red_position[1]] = 'R'
            # Move the blue marble
            new_blue_position = (blue_position[0] + dx, blue_position[1] + dy)
            if is_valid_position(new_blue_position, board) and new_blue_position != new_red_position:
                new_board[blue_position[0]][blue_position[1]] = '.'
                new_board[new_blue_position[0]][new_blue_position[1]] = 'B'
    return new_board, False

# Recursive function to perform a depth-first search on the game board
def search(board, depth):
    if depth == 10:
        # We've reached the maximum depth, so give up and return 0
        return 0
    success = False
    for move in MOVES:
        new_board, has_success = perform_move(board, move)
        if has_success:
            # We've found a solution!
            return depth + 1
        if new_board != board:
            result = search(new_board, depth + 1)
            if result > 0:
                # We've found a solution!
                return result
    return 0

# Read the input from the user
n, m = map(int, input().split())
board = []
for i in range(n):
    row = list(input().strip())
    board.append(row)

# Perform the search and print the result
result = search(board, (n, m))
print(result)