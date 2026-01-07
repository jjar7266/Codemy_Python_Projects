# Codemy.com - Instructor John Elder

# Course: Python Projects

# tic_tac_toe.py

# Modified instructors code to be more Pythonic and readable

# CLASS: TicTacToe

# PURPOSE:

#   Encapsulates the entire game:
#      * board state
#      * current player
#      * move handling
#      * win checking
#      * board printing

#    WHY A CLASS?
#      * Avoides global variables
#      * Keeps logic organized
#      * Easy to extend later (AI, replay, scoring)

# ======================================================================

# Import modules
import os

# FUNCTION: clear_screen()
# clears the terminal window before showing
# the game board or prompts

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class TicTacToe:

    def __init__(self):
        # The board is a list of 9 spaces

        self.board = [" " for _ in range(9)]
        self.current_player = "X"  # X always starts

    def print_board(self):
        # Display the board with numbers for empty spaces

        print()
        for row in range(3):
            line = []
            for col in range(3):
                index = row * 3 + col
                cell = self.board[index]

                # If the cell is empty, show its number(1-9)

                display = cell if cell != " " else str(index + 1)

                line.append(f" {display} ")
            print("|".join(line))
            if row < 2:
                print("---+---+---")
        print()
        

    def make_move(self, position: int) -> bool:
        # If the position is empty, place the player's mark

        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False
    
    def switch_player(self):
        # Toggle between X and O

        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> bool:
        # All winning combinations

        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        for a, b, c in wins:
            if (
                self.board[a] == self.board[b] == self.board[c]
                and self.board[a] != " "
            ):
                return True
            
        return False
    
    def is_full(self) -> bool:
        # If no spaces remain, the board is full

        return " " not in self.board
    

# FUNCTION: main()

# PURPOSE:

#   Runs the game loop:
#     * prints the board
#     * asks for a move
#     * validates input
#     * checks for win/tie
#     * switches players

# ====================================================================

def main():
    game = TicTacToe()

    while True:
        clear_screen()  # Clear terminal before showing the board

        game.print_board()
        print(f"Player {game.current_player}'s turn.")

        # Ask for a move

        choice = input("Choose a position (1-9): ")

        # Validate input

        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid input. Please choose a number 1-9.")
            continue

        position = int(choice) - 1  # Convert to 0-based index

        if not game.make_move(position):
            print("That spot is already taken.")
            continue

        # Check for winner

        if game.check_winner():
            clear_screen()
            game.print_board()
            print(f"Player {game.current_player} wins!")
            break

        # Check for tie

        if game.is_full():
            print("It's a tie!")
            break

        # Switch players

        game.switch_player()


if __name__ == "__main__":
    main()

