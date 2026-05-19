import time
import copy

# Import thuật toán của bạn (đảm bảo file của bạn có biến global state_count)
# Giả sử bạn đã sửa file AI để chạy trên virtual board (mảng dict) thay vì Tkinter Button
import minimax
import minimax_alpha_beta

def create_virtual_board(layout_strings):
    """Hàm hỗ trợ tạo bàn cờ ảo từ mảng chuỗi để dễ thiết lập test case"""
    board = []
    for row in layout_strings:
        board_row = []
        for char in row:
            text = "" if char == "." else char
            board_row.append({"text": text})
        board.append(board_row)
    return board

def print_board(board):
    for r in board:
        print(" ".join([c["text"] if c["text"] != "" else "." for c in r]))
    print("-" * 20)

def run_test(test_name, layout, max_depth=2):
    print(f"\n{'='*50}")
    print(f"Bài test: {test_name}")
    print(f"{'='*50}")
    
    board = create_virtual_board(layout)
    print("Trạng thái bàn cờ:")
    print_board(board)

    # 1. Test Minimax Thường
    print(">>> CHẠY MINIMAX THƯỜNG <<<")
    board_minimax = copy.deepcopy(board)
    minimax.state_count = 0 # Reset bộ đếm trạng thái (Bạn cần thêm biến global state_count vào file minimax.py giống bên alpha-beta)
    
    start_time_mm = time.time()
    # Gọi hàm AI của bạn (lượt máy đánh chữ O -> is_AI_O_turn = False theo code cũ của bạn)
    row_mm, col_mm = minimax.get_best_move(board_minimax)
    end_time_mm = time.time()
    time_mm = end_time_mm - start_time_mm
    
    # In kết quả Minimax
    print(f" - Nước đi chọn: ({row_mm}, {col_mm})")
    print(f" - Số trạng thái đã duyệt: {minimax.state_count}")
    print(f" - Thời gian chạy: {time_mm:.4f} giây")

    print("\n>>> CHẠY MINIMAX ALPHA-BETA <<<")
    # 2. Test Minimax Alpha-Beta
    board_ab = copy.deepcopy(board)
    minimax_alpha_beta.state_count = 0 # Reset bộ đếm
    
    start_time_ab = time.time()
    row_ab, col_ab = minimax_alpha_beta.get_best_move(board_ab)
    end_time_ab = time.time()
    time_ab = end_time_ab - start_time_ab
    
    # In kết quả Alpha-Beta
    print(f" - Nước đi chọn: ({row_ab}, {col_ab})")
    print(f" - Số trạng thái đã duyệt: {minimax_alpha_beta.state_count}")
    print(f" - Thời gian chạy: {time_ab:.4f} giây")
    
    # Thống kê so sánh
    print("\n--- KẾT LUẬN ---")
    if minimax.state_count > 0:
        saved_states = minimax.state_count - minimax_alpha_beta.state_count
        percent_saved = (saved_states / minimax.state_count) * 100
        print(f"Alpha-Beta cắt giảm được: {saved_states} trạng thái ({percent_saved:.2f}%)")
    if row_mm == row_ab and col_mm == col_ab:
        print("Hai thuật toán CHỌN CÙNG NƯỚC ĐI.")
    else:
        print("CẢNH BÁO: Hai thuật toán chọn nước đi KHÁC NHAU. Cần kiểm tra lại hàm đánh giá hoặc thứ tự duyệt nhánh!")


# 1. Trạng thái đầu ván
test_1 = [
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    "........."
]

# 2. Trạng thái giữa ván (phân tán)
test_2 = [
    ".........",
    ".........",
    "....O....",
    "...X.....",
    "....X....",
    ".....O...",
    ".........",
    ".........",
    "........."
]

# 3. Trạng thái máy có thể thắng ngay
test_3 = [
    ".........",
    ".........",
    ".........",
    "...OOO...", 
    "....X....",
    "...XX....",
    ".........",
    ".........",
    "........."
]

# 4. Trạng thái người chơi sắp thắng, máy CẦN CHẶN
test_4 = [
    ".........",
    ".........",
    ".........",
    "...XXX...", 
    ".........",
    "..OO.....",
    ".........",
    ".........",
    "........."
]

# 5. Trạng thái hai bên đều có cơ hội (nhiều nhánh)
test_5 = [
    ".........",
    "...O.....",
    "...X.O...",
    "..OXXX...",
    "..OO.....",
    ".........",
    ".........",
    ".........",
    "........."
]

if __name__ == "__main__":
    # Chạy lần lượt 5 test case với độ sâu = 2
    # Bạn có thể đổi độ sâu ở hàm get_best_move trong file gốc để test sâu hơn
    run_test("1. Trạng thái đầu ván", test_1)
    run_test("2. Trạng thái giữa ván", test_2)
    run_test("3. Trạng thái máy thắng ngay", test_3)
    run_test("4. Trạng thái chặn người chơi sắp thắng", test_4)
    run_test("5. Trạng thái tranh chấp phức tạp", test_5)