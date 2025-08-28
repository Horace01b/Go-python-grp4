from app.db import SessionLocal
from app.models.player import Player
from app.models.game import Game

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

def create_or_get_player(name: str):
    session = SessionLocal()
    player = session.query(Player).filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        session.add(player)
        session.commit()
        session.refresh(player)
        print(f" New player created: {player.name} ")
    else:
        print(f" Welcome back, {player.name}! ")
    return player

def create_game(black_player_id: int, white_player_id: int, board_size=9):
    session = SessionLocal()
    empty_board = [["." for _ in range(board_size)] for _ in range(board_size)]
    game = Game(
        black_player_id=black_player_id,
        white_player_id=white_player_id,
        board=empty_board
    )
    session.add(game)
    session.commit()
    session.refresh(game)
    print(f"New game started: Black={black_player_id}, White={white_player_id}")
    return game

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


def has_liberty(row, col):
    for nx, ny in get_neighbors(row, col):
        if board[nx][ny] == ".":
            return True
    return False

def check_captures(row, col, stone):
    opponent = "B" if stone == "W" else "W"
    for nx, ny in get_neighbors(row, col):
        if board[nx][ny] == opponent:
            if has_liberty(nx, ny) == False:   
                board[nx][ny] = "." 

def calculate_score(board):
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
    print()
    black_score, white_score = calculate_score(board)
    console.print(f"[bold blue]Final Score - Black: {black_score}, White: {white_score}[/]")
    if black_score > white_score:
        console.print("[bold green]Black wins![/]")
    elif white_score > black_score:
        console.print("[bold green]White wins![/]")
    else:
        console.print("[bold green]It's a tie![/]")
    # console.print("[bold magenta]Final scoring is not implemented in this version.[/]")
    console.print("[bold red]Thanks for playing![/]")

def play_game():
    current_player = "B"
    consecutive_passes = 0

    black_name = input("Enter name for Black player: ")
    black_player = create_or_get_player(black_name)

    white_name = input("Enter name for White player: ")
    white_player = create_or_get_player(white_name)

    console.print("[bold green]Welcome to Go![/]")

    while True:
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
        consecutive_passes = 0

        move = player_move.split()
        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            console.print("[bold red]Invalid input. Please enter row and column numbers.[/]")
            continue

        row = int(move[0])
        col = int(move[1])

        if place_stone(row, col, current_player):
            check_captures(row, col, current_player)
            current_player = "W" if current_player == "B" else "B"
        else:
            console.print("[bold red]Invalid move. That spot is already taken or out of bounds.[/]")
play_game()

