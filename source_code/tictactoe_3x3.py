import tkinter 
from minimaxTest import get_best_move

def set_title(row, column):
    global curr_player
    
    if game_over:
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player
    
    if curr_player == playerO:
        curr_player = playerX
    else: curr_player = playerO
    
    label["text"] = f"{curr_player}'s turn"
    
    check_winner()
    
    if not game_over and curr_player == playerO:
        window.update() # Optional: Force UI to update before AI freezes it to think
        
        # Pass the 'board' variable to the other file
        ai_row, ai_col = get_best_move(board) 
        
        if ai_row != -1 and ai_col != -1:
            # Re-use your own function to place the AI's move on the UI!
            set_title(ai_row, ai_col)
    
def check_winner():
    global turns, game_over
    turns += 1
    
    # Check row
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(
                text=f"{board[row][0]["text"]} is winner!",
                foreground=color_yellow
                )
            for column in range(3):
                board[row][column].config(foreground = color_yellow, background = color_light_gray)
            game_over = True
            return   

    # Check column
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(
                text=f"{board[0][column]["text"]} is winner!",
                foreground=color_yellow
                )
            for row in range(3):
                board[row][column].config(foreground = color_yellow, background = color_light_gray)
            game_over = True
            return  

    # Check diagonal
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
    and board[0][0]["text"] != ""):
        label.config(
            text=f"{board[0][0]["text"]} is winner!",
            foreground=color_yellow
            )
        for i in range(3):
            board[i][i].config(foreground = color_yellow, background = color_light_gray)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
    and board[0][2]["text"] != ""):
        label.config(
            text=f"{board[0][2]["text"]} is winner!",
            foreground=color_yellow
            )
        for i in range(3):
            board[i][2 - i].config(foreground = color_yellow, background = color_light_gray)
        game_over = True
        return
    
    if turns == 3 * 3:
        label.config(text="Tie!", foreground=color_yellow)
        game_over = True
    
def new_game():
    global turns, game_over, curr_player
    
    turns = 0
    game_over = False
    curr_player = playerX
    
    label.config(text=f"{curr_player}'s turn", foreground="white")
    for row in range(len(board)):
        for column in range(len(board)):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)
    
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame, 
    text = f"{curr_player}'s turn", 
    font = ("Consolas", 20),
    background = color_gray,
    foreground = "white"
)

label.grid(row = 0, column = 0, columnspan = len(board), sticky = "we")

for row in range(len(board)):
    for column in range(len(board)):
        board[row][column] = tkinter.Button(
            frame, 
            text = "",
            font = ("Consolas", 20, "bold"),
            background = color_gray,
            foreground = color_blue,
            width = 4,
            height = 1,
            command = lambda row = row, column = column: set_title(row, column)
        )
        board[row][column].grid(row = row + 1, column = column)
        
button = tkinter.Button(
    frame, 
    text = "Restart",
    font = ("Consolas", 20),
    background = color_gray,
    foreground = "white",
    command = new_game
)

button.grid(row = 10, column = 0, columnspan = len(board), sticky = "we")
        
frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()