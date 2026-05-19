# Đồ án Trí tuệ nhân tạo: Cờ Caro AI (Minimax & Alpha-Beta Pruning)

Dự án này là bài tập thực hành môn Trí tuệ nhân tạo, cài đặt trò chơi cờ Caro (kích thước 9x9) giữa người và máy. AI của máy tính được xây dựng dựa trên thuật toán tìm kiếm **Minimax** và được tối ưu hóa bằng kỹ thuật cắt tỉa **Alpha-Beta**.

## 👥 Thành viên thực hiện
* Nguyễn Đức Phong [23020694]

## 📂 Cấu trúc thư mục
Dự án được tổ chức như sau:

```text
23020694_CaroAI/
│
├── source_code/
│   ├── tictactoe.py            # File main (chứa giao diện sử dụng Tkinter và logic của game)
│   ├── minimax.py              # Thuật toán Minimax (Level 1)
│   ├── minimax_alpha_beta.py   # Thuật toán Minimax kết hợp cắt tỉa Alpha-Beta (Level 2)
│   └── benchmark.py            # File kiểm thử, so sánh hiệu năng (Level 3)
│
└── requirements.txt            # Chứa thông tin về các thư viện phụ thuộc