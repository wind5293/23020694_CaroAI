import time, copy
from source_code.minimax_alpha_beta import minimax, get_best_move, state_count

def make_board(moves, size=9):
    board = [[{"text": ""} for _ in range(size)] for _ in range(size)]
    for r, c, player in moves:
        board[r][c]["text"] = player
    return board

test_cases = [
    {
        "id": 1,
        "name": "Đầu ván (Early game)",
        "description": "Mới đánh vài nước, bàn cờ thưa, AI cần định hướng chiến lược.",
        "moves": [
            (4, 4, 'X'),
            (4, 5, 'O'),
            (3, 4, 'X'),
            (3, 5, 'O'),
        ],
    },
    {
        "id": 2,
        "name": "Giữa ván (Mid game)",
        "description": "Bàn cờ có nhiều quân, cả hai bên đang hình thành chuỗi.",
        "moves": [
            (4, 4, 'X'), (4, 5, 'O'), (4, 6, 'X'), (4, 7, 'O'),
            (5, 4, 'X'), (5, 5, 'O'), (5, 6, 'X'),
            (3, 3, 'O'), (3, 4, 'X'), (3, 5, 'O'),
            (6, 5, 'X'), (6, 6, 'O'),
        ],
    },
    {
        "id": 3,
        "name": "AI sắp thắng",
        "description": "O có 3 quân liên tiếp, AI cần đánh để thắng ngay.",
        "moves": [
            (4, 4, 'O'), (4, 5, 'O'), (4, 6, 'O'),   # O cần (4,7) để thắng
            (3, 3, 'X'), (3, 4, 'X'), (5, 5, 'X'),
        ],
    },
    {
        "id": 4,
        "name": "Người sắp thắng — AI phải chặn",
        "description": "X có 3 quân liên tiếp, AI cần chặn ngay tại (4,7).",
        "moves": [
            (4, 4, 'X'), (4, 5, 'X'), (4, 6, 'X'),   # X cần (4,7) để thắng
            (5, 5, 'O'), (5, 6, 'O'), (3, 3, 'O'),
        ],
    },
    {
        "id": 5,
        "name": "Hai bên đều có cơ hội tấn công",
        "description": "Trạng thái phức tạp, cả hai bên có chuỗi 2 quân nhiều hướng.",
        "moves": [
            (4, 4, 'X'), (4, 5, 'O'), (4, 6, 'X'),
            (5, 4, 'O'), (5, 5, 'X'), (5, 6, 'O'),
            (3, 4, 'X'), (3, 5, 'O'), (6, 4, 'X'),
            (6, 5, 'O'), (2, 3, 'X'), (7, 6, 'O'),
        ],
    },
]

def run_benchmark(board, depth, use_alpha_beta):
    import source_code.minimax_alpha_beta as mm
    mm.state_count = 0
    
    alpha = -float('inf') if use_alpha_beta else None
    beta  =  float('inf') if use_alpha_beta else None
    
    start = time.time()
    # Gọi get_best_move với mode tương ứng
    move = get_best_move(board, depth, use_alpha_beta)
    elapsed = time.time() - start
    
    return move, mm.state_count, elapsed

print(f"{'Case':<20} {'Depth'} {'Algo':<12} {'Move':<10} {'States':>10} {'Time(s)':>10}")
print("-" * 70)

for name, moves in test_cases.items():
    for depth in [1, 2, 3]:
        for algo, ab in [("Minimax", False), ("Alpha-Beta", True)]:
            board = make_board(moves)
            move, states, t = run_benchmark(board, depth, ab)
            print(f"{name:<20} {depth}     {algo:<12} {str(move):<10} {states:>10} {t:>10.4f}")