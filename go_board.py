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

# Print the board
def print_board():
    print("  " + " ".join(f"{column:2}" for column in range(board_size)))
    for row_index, row in enumerate(board):
        print(f"{row_index:2} " + " ".join(f"{cell:2}" for cell in row))


def place_stone(row, col, stone):
    if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == ".":
        board[row][col] = stone
        return True
    return False


def get_neighbors(row, col):
    neighbors = []
    if row > 0: 
        neighbors.append((row - 1, col))
    if row < board_size - 1: 
        neighbors.append((row + 1, col))
    if col > 0: 
        neighbors.append((row, col - 1))
    if col < board_size - 1: 
        neighbors.append((row, col + 1))
    return neighbors

def find_group(row, col, stone):
    group = [(row, col)]
    checked = []
    for x, y in group:
        if (x, y) not in checked:
            checked.append((x, y))
            for nx, ny in get_neighbors(x, y):
                if board[nx][ny] == stone and (nx, ny) not in group:
                    group.append((nx, ny))
    return group


def has_liberty(group):
    for x, y in group:
        for nx, ny in get_neighbors(x, y):
            if board[nx][ny] == ".":
                return True
    return False


def remove_group(group):
    for x, y in group:
        board[x][y] = "."


def check_captures(row, col, stone):
    opponent = "B" if stone == "W" else "W"
    for nx, ny in get_neighbors(row, col):
        if board[nx][ny] == opponent:
            group = find_group(nx, ny, opponent)
            if not has_liberty(group):
                remove_group(group)


def calculate_score(board):
    """Count stones for each player."""
    black_score = 0
    white_score = 0

    for row in board:
        for cell in row:
            if cell == "B":
                black_score += 1
            elif cell == "W":
                white_score += 1

    return black_score, white_score
  
def pass_game(current_player):
    console.print(f"[bold yellow]{current_player} has passed. Game was passed to the other player.[/]")
    return "W" if current_player == "B" else "B"

def end_game():
    console.print("[bold magenta]Both players have passed. The game is over.[/]")
    print_board()
    console.print("[bold magenta]Final scoring is not implemented in this version.[/]")
    console.print("[bold red]Thanks for playing![/]")

current_player = "B"
consecutive_passes = 0


current_player = "B"    
while True:
    console.print("[bold green]Welcome to Go![/]")
    print_board()
    print()
    console.print(f"Current player: [bold {'white on black' if current_player=='B' else 'black on white'}]{current_player}[/]")
    black_score, white_score = calculate_score(board)
    console.print(f"[bold blue]Score - Black: {black_score}, White: {white_score}[/]")

    console.print("[bold green]Enter your move (row col), 'pass' to pass, or 'q' to quit:[/]", end=" ")
    player_move = input().strip().lower()

    if player_move == "q":
        console.print("[bold red]Game over. Thanks for playing![/]")
        break

    if player_move == "pass":
        consecutive_passes += 1
        if consecutive_passes == 2:
            end_game()
            break
        current_player = pass_game(current_player)
        continue

    # Reset pass counter if a move is made
    consecutive_passes = 0

    move = player_move.split()
    if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
        console.print("[bold red]Invalid input. Please enter row and column numbers.[/]")
        continue

    if not move[0].isdigit() or not move[1].isdigit():
        console.print("[bold red]Invalid input. Please enter valid row and column numbers.[/]")
        continue


    row = int(move[0])
    col = int(move[1])

    if place_stone(row, col, current_player):
        check_captures(row, col, current_player)
        current_player = "W" if current_player == "B" else "B"
    else:
        console.print("[bold red]Invalid move. That spot is already taken or out of bounds.[/]")


    







