class TicTacToe:

    def __init__(self, board, current_state):

        self._board = [[[" "], [" "], [" "]],
                       [[" "], [" "], [" "]],
                       [[" "], [" "], [" "]]]

        self._current_state = "UNFINISHED"


    def make_move(self, row, column, player):
        tally = 0
        if row <= 2 and row >= 0:
            if column <=2 and column >=0:
                if player == "X" and self._board[row][column] == " ":
                    self._board[row][column] = "X"
                    tally += 1
                    for i in range(2):
                        if (self._board[0][i] == "X") and (self._board[1][i] == "X") and (self._board[2][i] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[i][0] == "X") and (self._board[i][1] == "X") and (self._board[i][2] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[0][0] == "X") and (self._board[1][1] == "X") and (self._board[2][2] == "X"):
                            self._current_state = "X_WON"
                        if (self._board[0][2] == "X") and (self._board[1][1] == "X") and (self._board[2][0] == "X"):
                            self._current_state = "X_WON"
                    if tally == 9 and self._current_state == "UNFINISHED":
                         self._current_state = "DRAW"
                    return True

                elif player == "O" and self._board[row][column] == " ":
                    self._board[row][column] = "O"
                    tally += 1
                    for i in range(2):
                        if (self._board[0][i] == "O") and (self._board[1][i] == "O") and (self._board[2][i] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[i][0] == "O") and (self._board[i][1] == "O") and (self._board[i][2] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[0][0] == "O") and (self._board[1][1] == "O") and (self._board[2][2] == "O"):
                            self._current_state = "O_WON"
                        if (self._board[0][2] == "O") and (self._board[1][1] == "O") and (self._board[2][0] == "O"):
                            self._current_state = "O_WON"
                    if tally == 9 and self._current_state == "UNFINISHED":
                        self._current_state = "DRAW"
                    return True
                else:
                    return False

        elif row > 2 or row < 0:
            return False

        elif column > 2 or row < 0:
            return False

        elif self._current_state == "X_WON" or self._current_state == "O_WON" or self._current_state == "DRAW":
             return False



    def get_current_state(self):
        return self._current_state
