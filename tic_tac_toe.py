
# Function for displaying the board
def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Function for choosing a symbol
def choose_symbol(symbols):
    while True:
        symbol = input("Player 1, choose your symbol (X/O): ").upper()

        if symbol == "X":
            return symbols[0]

        elif symbol == "O":
            return symbols[1]

        else:
            print("Invalid input. Please choose X or O.")


# Function for the player's move
def player_move(board, symbol):
    while True:
        try:
            position = int(input(f"Player {symbol}, choose a position (1-9): "))

            if position < 1 or position > 9:
                print("Please choose a number between 1 and 9.")
                continue

            if board[position - 1] not in ["X", "O"]:
                board[position - 1] = symbol
                break

            else:
                print("This position is already taken. Try again.")

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


# Function for checking if the current player has won
def check_winner(board, symbol):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for position_1, position_2, position_3 in winning_combinations:
        if (
            board[position_1] == symbol
            and board[position_2] == symbol
            and board[position_3] == symbol
        ):
            return True

    return False


# Function for checking if the game is a draw
def check_draw(board):
    for position in board:
        if position not in ["X", "O"]:
            return False

    return True


# Function for switching the current player
def switch_player(current_symbol):
    if current_symbol == "X":
        return "O"
    else:
        return "X"


# ----------------------------
# Main program
# ----------------------------

board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]

symbols = ["X", "O"]

player_1_symbol = choose_symbol(symbols)

if player_1_symbol == "X":
    player_2_symbol = "O"
else:
    player_2_symbol = "X"

print(f"Player 1: {player_1_symbol}")
print(f"Player 2: {player_2_symbol}")

current_symbol = player_1_symbol

while True:
    display_board(board)

    player_move(board, current_symbol)

    if check_winner(board, current_symbol):
        display_board(board)
        print(f"Player with {current_symbol} wins!")
        break

    if check_draw(board):
        display_board(board)
        print("The game is a draw!")
        break

    current_symbol = switch_player(current_symbol)