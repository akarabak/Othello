import othello
from othello_console import print_board

def test1():
    state = othello.GameState(4, 6, str(1), str(1), str(1))
    for i in range(4):
        state.putDiscTest(' B ', i, 5)
    state.putDiscTest(' W ', 3, 5)
    state.putDiscTest(' W ', 4, 5)
    state.putDiscTest(' B ', 4, 3)
    state.putDiscTest(' W ', 2, 3)
    state.switch_turn()
    try:
        state.putDisc(1,3)
    except:
        pass



    state._white_discs = 5
    state._black_discs = 5
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
            print('\n\n***7A disc is already in that cell***\n\n')
        except othello.InvalidMove:
            print('\n\n****That\'s an invalid move***\n\n')

    
def test2():

    state = othello.GameState(4, 4, str(1), str(1), str(1))
    state.putDiscTest(' B ', 1, 4)
    state.putDiscTest(' W ', 2, 4)
    state.putDiscTest(' B ', 3, 4)
    state.putDiscTest(' W ', 1, 3)
    state.putDiscTest(' B ', 2, 3)
    state.putDiscTest(' W ', 3, 3)
    state.putDiscTest(' B ', 1, 2)
    state.putDiscTest(' B ', 2, 2)
    state.putDiscTest(' W ', 3, 2)
    state.putDiscTest(' B ', 3, 1)
    state.putDiscTest(' W ', 1, 1)
    state.putDiscTest(' B ', 2, 1)
    state.putDiscTest(' W ', 4, 1)
    state.putDiscTest(' B ', 4, 2)
    state.putDiscTest(' W ', 4, 3)
    state.putDiscTest(' B ', 4, 4)


    state._white_discs = 5
    state._black_discs = 5
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
            print('\n\n***7A disc is already in that cell***\n\n')
        except othello.InvalidMove:
            print('\n\n****That\'s an invalid move***\n\n')

test1()








