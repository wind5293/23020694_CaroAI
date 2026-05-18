import math

def logicalEvalutionBoard(board):
    n = len(board)
    
    # Check row
    for r in range(n):
        for c in range(n - 3):
            if (board[r][c]["text"] == board[r][c+1]["text"] == board[r][c+2]["text"] == board[r][c+3]["text"] 
                and board[r][c]["text"] != ""):
                if board[r][c]["text"] == 'O':
                    return +10
                elif board[r][c]["text"] == 'X':
                    return -10
    
    # Check column
    for r in range(n - 3):
        for c in range(n):
            if (board[r][c]["text"] == board[r+1][c]["text"] == board[r+2][c]["text"] == board[r+3][c]["text"] 
                and board[r][c]["text"] != ""):
                if board[r][c]["text"] == 'O':
                    return +10
                elif board[r][c]["text"] == 'X':
                    return -10
        
    # Check diagonal
    for r in range(n - 3):
        for c in range(n - 3):
            if (board[r][c]["text"] == board[r+1][c+1]["text"] == board[r+2][c+2]["text"] == board[r+3][c+3]["text"] 
                and board[r][c]["text"] != ""):
                if board[r][c]["text"] == 'O':
                    return +10
                elif board[r][c]["text"] == 'X':
                    return -10
    
    for r in range(n - 3):
        for c in range(3, n):
            if (board[r][c]["text"] == board[r+1][c-1]["text"] == board[r+2][c-2]["text"] == board[r+3][c-3]["text"] 
                and board[r][c]["text"] != ""):
                if board[r][c]["text"] == 'O':
                    return +10
                elif board[r][c]["text"] == 'X':
                    return -10
                
    if not any(board[r][c]["text"] == "" 
               for r in range(n) 
               for c in range(n)):
        return 0
    
    return None
    
def minimax(board, depth, is_AI_O_turn):
    n = len(board)
    
    score = logicalEvalutionBoard(board)
    if score is not None:
        return score
    
    if is_AI_O_turn:
        best_score = -math.inf
        for r in range(n):
            for c in range(n):
                if (board[r][c]["text"] == ''):
                    board[r][c]["text"] = 'O'
                    current_score = minimax(board, depth + 1, False)
                    board[r][c]["text"] = ""
                    best_score = max(best_score, current_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(n):
            for c in range(n):
                if (board[r][c]["text"] == ''):
                    board[r][c]["text"] = 'X'
                    current_score = minimax(board, depth + 1, True)
                    board[r][c]["text"] = ""
                    best_score = min(best_score, current_score)
        return best_score
    
def get_best_move(board):
    n = len(board)
    best_score = -math.inf
    best_move_row = -1
    best_move_col = -1

    for r in range(n):
        for c in range(n):
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