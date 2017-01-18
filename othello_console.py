#Arman Karabakhtsyan 28152667 Project 4 Lab 2

import othello

def print_board(board : othello.GameState) -> None:
    '''Prints the board'''
    state = board.getBoard()
    for row in range(board.getRows()):
        print('{:2}|'.format(board.getRows() - row), end = '')
        for col in range(board.getColumns()):
            print(state[board.getRows() - row - 1][col], end = '')
            print('|', end = '')
        print('\n  ', end = '')
        print('-' * (board.getColumns() * 4))
    print('  ', end = '')
    for col in range(board.getColumns()):
        print(' {:3}'.format(col + 1), end = '')
    print()
    print('\nWhite discs {}, Black discs {}\n'.format(board.getWhiteDiscs(), board.getBlackDiscs()))

def user_input() -> othello.GameState:
    '''Handles are user input to initialize game'''
    while True:
        try:
            rows = int(input('How many rows? '))
        except:
            print('Input must be an integer')
        else:
            if rows >= 4 and rows <= 16 and rows%2 == 0:
                break
            else:
                print('Number of rows must be an even number between 4 and 16')
                
    while True:
        try:
            columns = int(input('How many colums? '))
        except:
            print('Input must be an integer')
        else:
            if columns >= 4 and columns <= 16 and columns%2 == 0:
                break
            else:
                print('Number of rows must be an even number between 4 and 16')

    while True:
        move = input('Which of the players will move first?\n'
                 + '1) White\n'
                 + '2) Black\n')
        if move == '1' or move == '2':
            break
        else:
            print('Choice must be 1 or 2\n')

    while True:
        topleft = input('Which color disc will be in the top-left position?\n'
                        + '1) White (default)\n'
                        + '2) Black\n')
        if topleft == '1' or topleft == '2':
            break
        else:
            print('Choice must be 1 or 2\n')

    while True:
        winning_condition = input('How is a winner determined?\n'
                                  + '1) The player with the most discs on the board at the end of the game\n'
                                  + '2) The player with the fewest discs on the board at the end of the game\n')
        if winning_condition == '1' or winning_condition == '2':
            break
        else:
            print('Choice must be 1 or 2\n')

    return othello.GameState(rows, columns, move, topleft, winning_condition)
        
if __name__ == '__main__':
    state = user_input()
    while True:
        print_board(state)
        if state.move_check() == 0:
            state.switch_turn()
            if state.move_check() == 0:
                state.GameOver()
                print('Game Over')
                print('The winner is: ' + state.getWinner())
                break
        print('Current player:' + state.getTurn())

        while True:
            try:
                column = int(input('Column: '))
                if column <= state.getColumns() and column > 0:
                    break
                else:
                    print('A column must be between 1 and', state.getColumns())
            except:
                print('The value must be an integer')
            

        while True:
            try:
                row = int(input('Row: '))
                if row <= state.getRows() and row > 0:
                    break
                else:
                    print('A row must be between 1 and', state.getRows())
            except:
                print('The value must be an integer')             
            
        try:
            state.putDisc(column, row)
        except othello.DiscPresent:
            print('\n\n***A disc is already in that cell***\n\n')
        except othello.InvalidMove:
            print('\n\n****That is an invalid move***\n\n')

        
            
    
