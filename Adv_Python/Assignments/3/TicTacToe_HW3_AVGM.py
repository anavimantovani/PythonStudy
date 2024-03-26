# Author: Ana Victoria Gomes Mantovani
# Date: 09/19/2023
# Program: Tic Tac Toe

import numpy as np

# Print the Tic Tac Toe board with row and column numbering
def print_board(board):
    
    # Print the column numbers
    print("  0   1   2")

    for i, row in enumerate(board):
        print(i, end=' ')  # Print the row number
        for j, cell in enumerate(row):
            print(cell, end=' ')
            if j < len(row) - 1:
                print("|", end=' ')
        print()  # Move to the next line

        if i < len(board) - 1:
            print("  " + "-" * 9)

# Check if a player has won
def check_winner(board, player):
    
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i] == player) or all(board[:, i] == player):
            return True
    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Check if the board is full
def is_full(board):
    return not any(' ' in row for row in board)

# Check if the user entered a valid move
def valid_move(move, board):
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

# Main program
def main():
    board = np.array([[' ']*3 for _ in range(3)])
    current_player = 'X'

    # Generate the board and start game
    while True:
        print_board(board)
        print()
        print(f"Player {current_player}'s turn")
        print()

        # Prompt user for their move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                print()
                move = (row, col)
                if valid_move(move, board):
                    break
                else:
                    print("Invalid move. Try again.")
                    print()
            except ValueError:
                print("Invalid input. Enter row and column as integers.")
                print()

        board[row][col] = current_player

        # Check if a player won
        if check_winner(board, current_player):
            print_board(board)
            print()
            print("----------------")
            print(f"Player {current_player}  wins!")
            print("----------------")
            print()
            break
        
        # If the board is full declare a draw
        elif is_full(board):
            print_board(board)
            print()
            print("------------")
            print("It's a draw!")
            print("------------")
            print()
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    main()
    