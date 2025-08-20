board_size = 9

# Initialize a Go board of size 9x9
board = []  

for _ in range(board_size):            
    row = []                           
    for _ in range(board_size):        
        row.append(".")                
    board.append(row)                  


# columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:board_size]
# print("   " + " ".join(columns))  
# def parse_move(move):
    # col_letter = move[0].upper()         # first character is the column
    # row_number = int(move[1:])           # rest is the row
    # col = ord(col_letter) - ord("A")     # convert A->0, B->1, etc.
    # row = row_number - 1                 # convert 1-based to 0-based index
    # return row, col
def print_board():
    print("  " + " ".join(f"{column:2}" for column in range(board_size)))
    # Print each row with row numbers
    for row_index, row in enumerate(board):
        print(f"{row_index:2} " + " ".join(f"{cell:2}" for cell in row))

def place_stone(row, col, stone):
    if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == ".":
        board[row][col] = stone
        return True
    return False

current_player = "B"
while True:
    print_board()
    print()
    print(f"Current player: {current_player}")
    print("Enter your move (row and column eg: 2 3) or 'q' to quit:")
    player_move = input().strip()

    if player_move.lower() == "q":
        print("Game over. Thanks for playing!")
        break

    move = player_move.split()
    if len(move) != 2:
        print("Invalid input. Please enter row and column numbers.")
        continue
    if not move[0].isdigit() or not move[1].isdigit():
        print("Invalid input. Please enter valid row and column numbers.")
        continue
    row = int(move[0])
    col = int(move[1])

    if place_stone(row, col, current_player):
        current_player = "W" if current_player == "B" else "B"
    else:
        print("Invalid move. That spot is already taken or out of bounds.")
