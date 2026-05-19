import math

state_count = 0

def logicalEvaluationBoard(board):
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

def heuristicEvaluation(board):
    n = len(board)
    total_score = 0
    
    # Hàm phụ để chấm điểm từng nhóm 4 ô
    def evaluate_window(window):
        score = 0
        count_O = window.count('O')
        count_X = window.count('X')
        count_empty = window.count('')

        # Máy có 4 quân liên tiếp: điểm rất lớn
        if count_O == 4:
            score += 100000
        # Người chơi có 4 quân liên tiếp: điểm rất nhỏ (âm lớn)
        elif count_X == 4:
            score -= 100000
        # Máy có 3 quân liên tiếp còn khả năng mở rộng: điểm cao
        elif count_O == 3 and count_empty == 1:
            score += 1000
        # Người chơi có 3 quân liên tiếp: điểm âm lớn để ưu tiên chặn
        # Chú ý: Trừ nặng hơn điểm cộng của AI để AI buộc phải chặn thay vì tấn công
        elif count_X == 3 and count_empty == 1:
            score -= 8000 
        # Máy có 2 quân liên tiếp: điểm dương nhỏ
        elif count_O == 2 and count_empty == 2:
            score += 10
        # Người chơi có 2 quân liên tiếp: điểm âm nhỏ
        elif count_X == 2 and count_empty == 2:
            score -= 10
            
        return score

    # Quét tất cả các hàng ngang (mỗi lần lấy 4 ô)
    for r in range(n):
        for c in range(n - 3):
            window = [board[r][c+i]["text"] for i in range(4)]
            total_score += evaluate_window(window)

    # Quét tất cả các cột dọc
    for r in range(n - 3):
        for c in range(n):
            window = [board[r+i][c]["text"] for i in range(4)]
            total_score += evaluate_window(window)

    # Quét đường chéo chính (\)
    for r in range(n - 3):
        for c in range(n - 3):
            window = [board[r+i][c+i]["text"] for i in range(4)]
            total_score += evaluate_window(window)

    # Quét đường chéo phụ (/)
    for r in range(n - 3):
        for c in range(3, n):
            window = [board[r+i][c-i]["text"] for i in range(4)]
            total_score += evaluate_window(window)

    return total_score

def get_candidate_moves(board):
    n = len(board)
    candidates = set()
 
    for r in range(n):
        for c in range(n):
            if board[r][c]["text"] != "":
                for dr in range(-2, 3):
                    for dc in range(-2, 3):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and board[nr][nc]["text"] == "":
                            candidates.add((nr, nc))
 
    # Đầu game chưa có quân nào → đánh giữa bàn
    if not candidates:
        mid = n // 2
        candidates.add((mid, mid))
 
    return candidates
    
def minimax(board, depth, max_depth, alpha, beta, is_AI_O_turn):
    n = len(board)
    global state_count
    state_count += 1
    
    # Đánh giá liệu có ai thắng chưa
    terminal_score = logicalEvaluationBoard(board)
    if terminal_score is not None:
        if terminal_score == 10: return 1000000 - depth * 100000
        if terminal_score == -10: return -1000000 + depth * 100000
        return 0 # Hòa

    if depth == max_depth:
        return heuristicEvaluation(board)
    
    candidates = get_candidate_moves(board)
 
    if is_AI_O_turn:
        best = -math.inf
        for r, c in candidates:
            board[r][c]["text"] = 'O'
            score = minimax(board, depth + 1, max_depth, alpha, beta, False)
            board[r][c]["text"] = ""
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha: 
                break
        return best
    else:
        best = math.inf
        for r, c in candidates:
            board[r][c]["text"] = 'X'
            score = minimax(board, depth + 1, max_depth, alpha, beta, True)
            board[r][c]["text"] = ""
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha: 
                break
        return best
    
def get_best_move(board):
    n = len(board)
    best_score = -math.inf
    best_move_row, best_move_col = -1, -1 
    max_depth = 2

    candidates = get_candidate_moves(board)
    for r, c in candidates:
        board[r][c]["text"] = "O"
        score = minimax(board, 0, max_depth, -math.inf, math.inf, False)
        board[r][c]["text"] = ""
        if score > best_score:
            best_score = score
            best_move_row, best_move_col = r, c
            
    print(f"AI chọn: ({best_move_row}, {best_move_col}) | score = {best_score}")
    return best_move_row, best_move_col