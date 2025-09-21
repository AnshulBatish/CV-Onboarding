class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_winner = None  # Keep track of the winner!
        self.current_player = 'X'
        self.game_over = False
    
    def print_board(self) -> None:
        for row in range(3):
            print(f"| {self.board[row * 3]} | {self.board[row*3 + 1]} | {self.board[row*3 + 2]} |")
            print("-------------")
    
    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
            
    def check_winner(self):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8), # Check rows
                        (0,3,6), (1,4,7), (2,5,8), # Check columns
                        (0,4,8), (2,4,6)]          # Check diagonals
        for win in win_patterns:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]] != ' ':
                return True
        return False
    
    def play_turn(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.current_winner = self.current_player
                self.game_over = True   
            self.change_player()
            return True
        return False
                
    def play_game(self):
        self.print_board()
        while not self.game_over:
            try:
                move = int(input(f"Player {self.current_player}, please inform which position you want to play your piece (1 - 9): ")) - 1
                if 0 <= move <= 8 and self.play_turn(move):
                    self.print_board()
                else:
                    print("There is already a piece there. Please pick another empty spot between 1 and 9.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9")
        print(f"The winner is {self.current_winner}!")
            
            
Game1 = TicTacToe()
Game1.play_game()    