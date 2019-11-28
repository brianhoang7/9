# Author: Brian Hoang
# Date: 11/27/2019
# Description: tic tac toe class that establishes 3x3 board and allows players to place pieces on board until game is won or drawn


class TicTacToe:
    #init method to initialize game board and game state
    def __init__(self):
        self._board = [[[" "], [" "], [" "]],
                       [[" "], [" "], [" "]],
                       [[" "], [" "], [" "]]]
        self._current_state = "UNFINISHED"

    #method that takes row and column moves and player turn as parameter
    def make_move(self, row, column, player):
        #tally for counting turns to determine draw
        tally = 0
        #condition to check for row/column inputs outside of the game board
        if row <= 2 and row >= 0:
            if column <=2 and column >=0:
                #checks for player turn and if board position isn't filled
                if player == "X" and self._board[row][column] == " ":
                    #marks board with player X if conditions are met
                    self._board[row][column] = "X"
                    #adds tally for draw check
                    tally += 1
                    #loop for checking the board for winning rows/columns
                    for i in range(2):
                        if (self._board[0][i] == "X") and (self._board[1][i] == "X") and (self._board[2][i] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[i][0] == "X") and (self._board[i][1] == "X") and (self._board[i][2] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[0][0] == "X") and (self._board[1][1] == "X") and (self._board[2][2] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[0][2] == "X") and (self._board[1][1] == "X") and (self._board[2][0] == "X"):
                            self._current_state = "X_WON"
                    #when tally hits 9 and game state is still unfinished, game will end in a draw
                    if tally == 9 and self._current_state == "UNFINISHED":
                         self._current_state = "DRAW"
                    return True
            return True
        #checking same conditions for O player
        if row <= 2 and row >= 0:
            if column <= 2 and column >= 0:
                # checks for player turn and if board position isn't filled
                if player == "O" and self._board[row][column] == " ":
                    # marks board with player O if conditions are met
                    self._board[row][column] = "O"
                    # adds tally for draw check
                    tally += 1
                    # loop for checking the board for winning rows/columns
                    for i in range(2):
                        if (self._board[0][i] == "O") and (self._board[1][i] == "O") and (self._board[2][i] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[i][0] == "O") and (self._board[i][1] == "O") and (self._board[i][2] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[0][0] == "O") and (self._board[1][1] == "O") and (self._board[2][2] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[0][2] == "O") and (self._board[1][1] == "O") and (self._board[2][0] == "O"):
                            self._current_state = "O_WON"
                    # when tally hits 9 and game state is still unfinished, game will end in a draw
                    if tally == 9 and self._current_state == "UNFINISHED":
                        self._current_state = "DRAW"
                    return True
            return True
        #returns false if input is off of board
        elif row > 2 or row < 0:
            return False
        #returns false if column input is off board
        elif column > 2 or row < 0:
            return False
        #returns false if player input is not X or O
        elif player != "X" or player != "O":
            return False
        #returns false if game is won or drawn
        elif self._current_state == "X_WON" or self._current_state == "O_WON" or self._current_state == "DRAW":
             return False


    #get method to return current state of game
    def get_current_state(self):
        return self._current_state

