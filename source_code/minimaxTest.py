import math

def logicalBoardEvaluation(board):    
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
        and board[row][0]["text"] != ""):
            if board[row][0]["text"] == 'O': 
                return +10
            elif board[row][0]["text"] == 'X':
                return -10
            
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] 
        and board[0][column]["text"] != ""):
            if board[0][column]["text"] == 'O': 
                return +10
            elif board[0][column]["text"] == 'X':
                return -10
            
    # Check diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
    and board[0][0]["text"] != ""):
        if board[0][0]["text"] == "O": 
            return +10
        elif board[0][0]["text"] == "X": 
            return -10
        
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
    and board[0][2]["text"] != ""):
        if board[0][2]["text"] == "O": 
            return +10
        elif board[0][2]["text"] == "X": 
            return -10
    
    empty_cells = 0
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] == "": 
                empty_cells += 1
    if empty_cells == 0: 
        return 0
    
    return None

def minimax(board, depth, is_AI_O_turn):
    score = logicalBoardEvaluation(board)
    if score is not None:
        return score

    if is_AI_O_turn:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c]["text"] == "":
                    board[r][c]["text"] = "O"
                    current_score = minimax(board, depth + 1, False)
                    board[r][c]["text"] = "" # Undo
                    best_score = max(best_score, current_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c]["text"] == "":
                    board[r][c]["text"] = "X"
                    current_score = minimax(board, depth + 1, True)
                    board[r][c]["text"] = ""
                    best_score = min(best_score, current_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move_row = -1
    best_move_col = -1

    for r in range(3):
        for c in range(3):
            if board[r][c]["text"] == "":
                board[r][c]["text"] = "O"
                score = minimax(board, 0, False)
                board[r][c]["text"] = "" # Undo
                
                if score > best_score:
                    best_score = score
                    best_move_row = r
                    best_move_col = c
    print(best_move_row, best_move_col, best_score)
    return best_move_row, best_move_col
        