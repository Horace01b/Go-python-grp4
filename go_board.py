from rich.console import Console


console = Console()

board_size = 9

# Initialize a Go board of size 9x9
board = []  

for _ in range(board_size):            
    row = []                           
    for _ in range(board_size):        
        row.append(".")                
    board.append(row)                  

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
    console.print("[bold green]Welcome to Go![/]")
    print_board()
    print()
    console.print(f"Current player: [bold {'white on black' if current_player=='B' else 'black on white'}]{current_player}[/]")

    console.print("[bold green]Enter your move (row and column eg: 2 3) or 'q' to quit:[/]", end=" ")
    player_move = input().strip()

    if player_move.lower() == "q":
        console.print("[bold red]Game over. Thanks for playing![/]")
        break

    move = player_move.split()
    if len(move) != 2:
        console.print("[bold red]Invalid input. Please enter row and column numbers.[/]")
        continue
    if not move[0].isdigit() or not move[1].isdigit():
        console.print("[bold red]Invalid input. Please enter valid row and column numbers.[/]")
        continue
    row = int(move[0])
    col = int(move[1])
    
    if place_stone(row, col, current_player):
        if current_player == "B":
            current_player =  "W"
        else:
            current_player = "B"
    else:
        console.print("[bold red]Invalid move. That spot is already taken or out of bounds.[/]")


