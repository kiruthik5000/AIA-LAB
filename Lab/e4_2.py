import math

def empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                cells.append((i, j))
    return cells

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != "_":
            return row[0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "_":
            return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return board[0][2]
    return None

def is_full(board):
    return len(empty_cells(board)) == 0

def minimax(board, is_max):

    winner = check_winner(board)
    
    if winner == "O": return 1
    if winner == "X": return -1
    
    if is_full(board): return 0

    best = -math.inf if is_max else math.inf

    for (i, j) in empty_cells(board):
        board[i][j] = "O" if is_max else "X"
        score = minimax(board, not is_max)
        board[i][j] = "_"

        best = max(best, score) if is_max else min(best, score)

    return best


board = [
    ["X", "O", "X"],
    ["_", "O", "_"],
    ["_", "_", "_"]
]

print("Move  |  Score")
print("----------------")

for (i, j) in empty_cells(board):
    board[i][j] = "O"
    score = minimax(board, False)
    board[i][j] = "_"
    print(f"({i},{j})   ->   {score}")