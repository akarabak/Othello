#Arman Karabakhtsyan 28152667, Project 5, Lab 2


from collections import namedtuple

EMPTY = '   '
BLACK = ' B '
WHITE = ' W '

Coordinates = namedtuple('Coordinates', 'column row')

class GameState:
    def __init__(self, columns : int, rows : int, start : str, topleft : str, winning_condition : str) -> None:
        '''Sets up game state with specified parameters'''
        self._rows = rows
        self._cols = columns
        self._topleft = topleft
        self._winning_condition = winning_condition
        self._white_discs = 0
        self._black_discs = 0
        self._gamestate = []
        self._gameover = False
        if start == '1':
            self._turn = WHITE
        else:
            self._turn = BLACK
        for row in range(self._rows):
            self._gamestate.append([])
            for col in range(self._cols):
                self._gamestate[row].append(EMPTY)
        self._prep_game()



    def _prep_game(self) -> None:
        '''Used to prepare the game'''
        if self._topleft == '1':
            self._gamestate[self._rows//2][self._cols//2 - 1] = WHITE
            self._gamestate[self._rows//2 - 1][self._cols//2] = WHITE
            self._gamestate[self._rows//2][self._cols//2] = BLACK
            self._gamestate[self._rows//2 - 1][self._cols//2 - 1] = BLACK
        else:
            self._gamestate[self._rows//2][self._cols//2 - 1] = BLACK
            self._gamestate[self._rows//2 - 1][self._cols//2] = BLACK
            self._gamestate[self._rows//2][self._cols//2] = WHITE
            self._gamestate[self._rows//2 - 1][self._cols//2 - 1] = WHITE
        self._white_discs = 2
        self._black_discs = 2

    def getBoard(self) -> list:
        '''Returns the current game state to the caller'''
        return self._gamestate

    def switch_turn(self) -> None:
        '''Switches the turn to an opposite player'''
        if self._turn == BLACK:
            self._turn = WHITE
        else:
            self._turn = BLACK

    def GameOver(self) -> None:
        '''Sets gameover variable to True'''
        self._gameover = True

    def getWinner(self) -> 'winner str':
        '''Returns a winner, NONE if tie'''
        if self._winning_condition == '1':
            if self._white_discs > self._black_discs:
                return WHITE
            elif self._white_discs == self._black_discs:
                return 'TIE'
            else:
                return BLACK
        else:
            if self._white_discs < self._black_discs:
                return WHITE
            elif self._white_discs == self._black_discs:
                return NONE
            else:
                return BLACK

    def putDiscTest(self, turn : str, col : int, row : int) -> None:
        '''Used for testing'''
        self._gamestate[row - 1][col - 1] = turn

    def _add_disc(self) -> None:
        '''Increases the amount of player's discs by one'''
        if self._turn == WHITE:
            self._white_discs += 1
        else:
            self._black_discs += 1

    def _remove_disc(self) -> None:
        '''Reduces the number of opponent's discs by one'''
        if self._turn == WHITE:
            self._black_discs -= 1
        else:
            self._white_discs -= 1

    def putDisc(self, col : int, row : int) -> None:
        '''Used by a user to drop a disc. Runs all necessary checks and raises exceptions'''
        if not self._gameover:
            if (col <= self._cols and col > 0) and (row <= self._rows and row > 0):
                if self._gamestate[row - 1][col - 1] == EMPTY:
                    to_flip = self._discs_to_flip(col - 1, row - 1)
                    if to_flip != []:
                        self._add_disc()
                        for i in to_flip:
                            self._add_disc()
                            self._remove_disc()
                        self._gamestate[row - 1][col - 1] = self._turn
                        for coordinate in to_flip:
                            self._gamestate[coordinate.row][coordinate.column] = self._turn
                        self.switch_turn()
                    else:
                        raise InvalidMove()
                else:
                    raise DiscPresent()
            else:
                raise InvalidMove()
        else:
            raise InvalidMove()
                    
    

    def move_check(self) -> int:
        '''Returns the amount of moves the current player has'''
        possible_moves = 0
        for row in range(self._rows):
            for col in range(self._cols):
                if self._gamestate[row][col] == EMPTY:
                    if self._discs_to_flip(col, row) != []:
                        possible_moves += 1
        return possible_moves

    def _discs_to_flip(self, column : int, row : int) -> [Coordinates]:
        '''Returns a list of disc coordinates to flip'''
        result = []
        result.extend(self._diagonal_check(column, row))
        result.extend(self._horizontal_check(column, row))
        result.extend(self._vertical_check(column, row))

        return result

    def _for_check(self, column : int, row : int, for_range : int, delta1 : int, delta2 : int) -> [Coordinates]:
        '''Delta1 is for columns, Delta2 for rows.
           Both must be either -1, 0, or 1, where -1 meast subtract, 1 add, and 0 don't change'''

        to_flip = []
        count = 0
        count_check = -1
        for count in range(1, for_range):
            if self._gamestate[row + count * delta2][column + count * delta1] != self._turn and self._gamestate[row + count * delta2][column + count * delta1] != EMPTY:
                to_flip.append(Coordinates(column + count * delta1, row + count * delta2))
                count_check = count
            else:
                break
        
        if self._row_and_col_legal(column + count * delta1, row + count * delta2):
            if self._gamestate[row + count * delta2][column + count * delta1] == self._turn:
                return to_flip
            else:
                return []
        else:
            return []

    def _row_and_col_legal(self, col : int, row : int) -> bool:
        '''Returns true if given col and row are less or equal than maximum grade'''
        return row < self._rows and col < self._cols

     

    def _horizontal_check(self, column : int, row : int) -> [Coordinates]:
        '''Checks whether there are opponent discs are located horizontally with own disc on the end'''
        result = []
        result.extend(self._for_check(column, row, column + 1, -1, 0))
        result.extend(self._for_check(column, row, self._cols - column, 1, 0,))
        return result

    def _vertical_check(self, column : int, row : int) -> [Coordinates]:
        '''Checks whether there are opponent discs are located vertically with own disc on the end'''
        
        result = []
        result.extend(self._for_check(column, row, row + 1, 0, -1))
        result.extend(self._for_check(column, row, self._rows - row, 0, 1))
        return result

    def _diagonal_check(self, column : int, row : int) -> [Coordinates]:
        '''Checks whether there are opponent discs are located diagonally with own disc on the end'''
        
        result = []
        result.extend(self._for_check(column, row, min(self._rows - row, self._cols - column), 1, 1))
        result.extend(self._for_check(column, row, min(row + 1, column + 1), -1, -1))
        result.extend(self._for_check(column, row, min(row + 1, self._cols - column), 1, -1))
        result.extend(self._for_check(column, row, min(self._rows - row, column + 1), -1, 1))
        return result



    def getRows(self) -> int:
        '''Return the number of rows on the board'''
        return self._rows

    def getColumns(self) -> int:
        '''Return number of columns on the board'''
        return self._cols

    def getTopleft(self) -> str:
        '''Return the top left disc that game started with'''
        return self._topleft

    def getWinningCondition(self) -> str:
        '''Return the winning condition'''
        return self._winning_condition

    def getTurn(self) -> str:
        '''Return the current turn'''
        return self._turn

    def getWhiteDiscs(self) -> int:
        '''Return the amount of black discs on the board'''
        return self._white_discs

    def getBlackDiscs(self) -> int:
        '''Return the amount of black discs on the board'''
        return self._black_discs




class DiscPresent(Exception):
    '''An exception that there is a different disc preset in the field'''
    pass

class InvalidMove(Exception):
    '''An exception that the move was invalid'''
    pass
