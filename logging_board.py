from board import Board

class LoggingBoard(Board):
    """
    A subclass of Board that will log a players moves and prints the log when the game is over.

    Methods:
    - __init__(): Initializes the log and board list.
    - claim_square(player,index): Records the player's moves in the log list.
    - get_winner(): Records the winner in the log list.
    - game_over(): Prints the log list when the game ends.
    """
    def __init__(self):
        super.__init__()
        self.log = []

    def claim_square(self, player, index):
        """
        Records the player's moves in the log list.
        """
        super().claim_square(index,player)
        self.log.append(f"{player} selects square {index}")

    def get_winner(self):
        """
        Records the winner in the log list.
        """
        winner = super().get_winner()
        if winner:
            self.log.appen(f"{winner} wins")
        return winner
    
    def game_over(self):
        """
        Prints the log list when the game ends.
        """
        game_is_over = super().game_over()
        if game_is_over:
            for i in self.log:
                print(i)
        return game_is_over