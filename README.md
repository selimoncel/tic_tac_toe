# Tic Tac Toe 

A clean, cross-platform command-line Tic Tac Toe written in Python.  
Features input validation, winner detection, draw handling, and a replay loop with automatic console clear on restart.

## Demo

```text
   1   2   3
1    │   │
  ───┼───┼───
2    │   │
  ───┼───┼───
3    │   │

Features:
-Safe input parsing with helpful error messages

-Prevents overwriting taken cells

-Winner detection (rows, columns, diagonals)

-Draw detection after 9 valid moves

-Replay support (y to play again) with auto console clear

Requirements:
-Python 3.8+
-No external dependencies required.

Getting Started:
# 1) Clone or download this repository
git clone https://github.com/<selimoncel>/tic_tac_toe.git
cd tic_tac_toe

# 2) (Optional) Create & activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Run
python main.py
On Windows, console clear uses cls. On macOS/Linux, it uses clear.

Project Structure:

tic-tac-toe-cli/
├─ .gitignore
├─ LICENSE
├─ README.md
└─ tictactoe.py

How to Play:
-Players take turns entering their move as row col (e.g., 2 3).

-Valid rows/cols are 1..3.

-The game ends when a player wins or the board is full (draw).

-After each game, choose y to replay or n to exit.

Troubleshooting:
-Terminal does not clear on replay: Ensure you are using a standard terminal. On some IDE consoles, clear/cls may not behave like a true terminal.

-ValueError on input: Enter exactly two integers separated by space (e.g., 1 1).

