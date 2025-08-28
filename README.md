# Go-python-grp4

A simple implementation of the classic board game Go, built with Python, SQLAlchemy, and Alembic for database migrations.

## Features

- Play Go on a 9x9 board in the terminal
- Player management with persistent storage
- Game state and scoring
- Database-backed using PostgreSQL (or compatible DB)

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL (or compatible database)
- [pipenv](https://pipenv.pypa.io/en/latest/) for dependency management
- [rich](https://rich.readthedocs.io/en/stable/) library for enhanced terminal output

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Go-python-grp4.git
   cd Go-python-grp4
   ```

2. **Install dependencies:**
   ```sh
   pipenv install
   pipenv install rich
   ```

### Usage

Make sure you are inside the pipenv virtual environment before running the project:

```sh
pipenv shell
```

Then start the game:

```sh
python go_board.py
```

## Basic Rules of Go

- The game is played on a 9x9 grid by two players: Black and White.
- Players take turns placing a stone of their color on an empty intersection.
- Stones are captured and removed from the board if they are completely surrounded by the opponent's stones.
- The goal is to control the most territory by surrounding empty spaces and capturing opponent stones.
- Players may pass their turn; the game ends when both players pass consecutively.
- The winner is determined by counting controlled territory and captured stones.

## Contributors

- Horace Kauna
- Cynthia Mugo
- Irene Murage
- Ian Mabruk
- Wayne Muongi