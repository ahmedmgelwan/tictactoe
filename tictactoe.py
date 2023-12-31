# Design the game board as a 3x3 list of lists. Each element in the list represents a square on the board and is initially set to an empty string.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Create a function to print the game board to the console. This function should take the game board as a parameter and use loops to iterate through the rows and columns of the board, printing each square in the appropriate location.


def print_board(board):
    print('+'+'---+'*3)
    for row in board:
        for val in row:
            print(f'| {val} ', end='')
        print('|\n+'+'---+'*3)


# Create a function to handle player moves. This function should take the game board and the current player's symbol as parameters, prompt the player for their move (using input()), and update the game board with the player's symbol in the appropriate location.


current_player = input('Player: ').upper()
if current_player != 'X' or current_player != 'O':
    print('Player must be X or O')
    current_player = input('Player: ').upper()

def get_input(board):
    row = int(input('Enter row number [1-3]: ')) - 1
    col = int(input('Enter column number [1-3]: ')) - 1
    return row, col
def player_move(board):
    try:
        row, col = get_input(board=board)
        if 0 <= row <=2 and  0 <= col <=2:
            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print('You can not go to this square')
                row, col = get_input(board)
                if 0 <= row <=2 and  0 <= col <=2:
                    if board[row][col] == ' ':
                        board[row][col] = current_player
        else:
            print('Invalid Input, Value must be a number between 1 and 3')

    except ValueError:
        print('Invalid Input, Value must be a number between 1 and 3 not chars')




def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'

    else:
        current_player = 'X'


# Create a function to check for a win. This function should take the game board and the current player's symbol as parameters and check if any of the rows, columns, or diagonals of the board contain three of the player's symbols in a row.
game_running = True


def check_win(board, current_player):
    global game_running
    # Check for rows
    for row in board:
        if all(i == current_player for i in row):
            game_running = False
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player:
            game_running = False
            return True

    # Check for diagonals
    # main_diagonal
    if all(board[i][i] == current_player for i in range(3)):
        game_running = False
        return True
    # secondary_diagonal
    if all(board[i][2 - i] == current_player for i in range(3)):
        game_running = False
        return True


# Create a function to check for a tie. This function should take the game board as a parameter and check if every square on the board has been filled.
def check_tie(board):
    for row in board:
        if any(square == ' ' for square in row):
            return False
    return True


# Create a main game loop that alternates between the two players. In each iteration of the loop, print the current state of the game board, prompt the current player for their move, update the game board with the player's symbol, and check if the game has been won or tied. If the game has been won or tied, end the loop and print the appropriate message. Test the game by playing it and checking that it correctly handles player moves, checks for wins and ties, and prints the appropriate messages. Debug any issues that arise.

while game_running:
    print(f'Current Player: {current_player}')
    print_board(board=board)
    player_move(board)
    if check_win(board, current_player):
        print_board(board)
        print(f'{current_player} has win (:')
    if check_tie(board)and not check_win(board, current_player):
        print_board(board)
        print('tie')
        break
    switch_player()
