#Arman Karabakhtsyan 28152667, Project 5, Lab 2

import tkinter
import othello
import disc_model

class OthelloApplication:
    def __init__(self) -> None:
        '''Initializes a game and brings up selection window'''
        self._menu_window = tkinter.Tk()
        self._menu_window.title('Othello Game Selection Menu')
        self._menu_window.resizable(0,0)

        self._rowLabel = tkinter.Label(master = self._menu_window, text = 'How many rows?')
        self._rowLabel.grid(row = 0, column = 0, sticky = tkinter.W, padx = 20)
        
        choices = (4, 6, 8, 10, 12, 14, 16)
        self._rowVar = tkinter.IntVar()
        self._rowVar.set(choices[0])
        self._row_selection = tkinter.OptionMenu(self._menu_window, self._rowVar, *choices)
        self._row_selection.grid(row = 0, column = 1, padx = 20, pady = 10)

        self._colLabel = tkinter.Label(master = self._menu_window, text = 'How many columns?')
        self._colLabel.grid(row = 1, column = 0, sticky = tkinter.W, padx = 20)

        self._colVar = tkinter.IntVar()
        self._colVar.set(choices[0])
        self._col_selection = tkinter.OptionMenu(self._menu_window, self._colVar, *choices)
        self._col_selection.grid(row = 1, column = 1, sticky = tkinter.E, padx = 20)


        self._startLabel = tkinter.Label(master = self._menu_window, text = 'Which player starts the game?'
                                         +'\n1) White'
                                         +'\n2) Black')
        self._startLabel.grid(row = 2, column = 0, sticky = tkinter.W, padx = 20)

        self._startVar = tkinter.StringVar()
        self._startVar.set(1)
        self._start_selection = tkinter.OptionMenu(self._menu_window, self._startVar, 1, 2)
        self._start_selection.grid(row = 2, column = 1, sticky = tkinter.E, padx = 20)

        self._topleftLabel = tkinter.Label(master = self._menu_window, text = 'Which player starts in top left corner?'
                                           +'\n1) White'
                                           +'\n2) Black')
        self._topleftLabel.grid(row = 3, column = 0, sticky = tkinter.W, padx = 20)
        
        self._topleftVar = tkinter.StringVar()
        self._topleftVar.set(1)
        self._topleft_selection = tkinter.OptionMenu(self._menu_window, self._topleftVar, 1, 2)
        self._topleft_selection.grid(row = 3, column = 1, sticky = tkinter.E, padx = 20)

        self._winLabel = tkinter.Label(master = self._menu_window, text = 'Winning condition:'
                                       +'\n1) The one with highest number of discs'
                                       +'\n2) The one with lowest number of discs')
        self._winLabel.grid(row = 4, column = 0, sticky = tkinter.W, padx = 20)
                                       
        self._winVar = tkinter.StringVar()
        self._winVar.set(1)
        self._winning_condition_selection = tkinter.OptionMenu(self._menu_window, self._winVar, 1, 2)
        self._winning_condition_selection.grid(row = 4, column = 1)

        self._DoneButton = tkinter.Button(self._menu_window, text = 'Done', command = self._menu_window.destroy) #close the selection menu
        self._DoneButton.grid(row = 5, column = 0, columnspan = 2, sticky = tkinter.S)
        
        self._menu_window.mainloop()     

        
    def start(self) -> None:
        '''Needs to be run to draw the othello board'''

        self._gamestate_setup()
        self._setup_game()
        self._window.mainloop()

    def _setup_game(self) -> None:
        '''Sets up the board'''
        self._window = tkinter.Tk()
        self._window.title('Othello Game')
        
        self._window.columnconfigure(0, weight = 1)
        self._window.rowconfigure(1, weight = 10)
    

        self._title = tkinter.Label(master = self._window, text = 'Othello Game', font = ('Helvetica', '20'))
        self._title.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.W + tkinter.E, columnspan = 2)
                    
        self._canvas = tkinter.Canvas(master = self._window, background = 'green')
        self._canvas.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E, columnspan = 2)       
        self._canvas.grid(
            row = 1, column = 0, columnspan = 2, padx = 20, pady = 20,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self._canvas_resized)
        self._canvas.bind('<Button-1>', self._canvas_clicked)
        
        self._whiteMessage = tkinter.Label(master = self._window, text = '# White discs: {}'.format(self._gamestate.getWhiteDiscs()),
                                           font = ('Helvetica', '12'))
        self._whiteMessage.grid(row = 2, column = 0, sticky = tkinter.W, padx = 10, pady = 10)

        
        self._blackMessage = tkinter.Label(master = self._window, text = '# Black discs: {}'.format(self._gamestate.getBlackDiscs()),
                                           font = ('Helvetica', '12'))
        self._blackMessage.grid(row = 2, column = 1, sticky = tkinter.E, padx = 10, pady = 10)

        self._message_box = tkinter.Label(master = self._window, text = '{}'.format(self.getTurn()), font = ('Helvetica', '14'))
        self._message_box.grid(row = 3, column = 0, columnspan = 2, sticky = tkinter.E + tkinter.W)

        self._x_radius_frac = 1 / (self._colVar.get() * 2 + 2) #find vertical and horizontal radius of the disk based on current row and column amount
        self._y_radius_frac = 1 / (self._rowVar.get() * 2 + 2)


    

    def _gamestate_setup(self) -> None:
        '''Initalizes a game logic state'''
        self._gamestate = othello.GameState(self._colVar.get(), self._rowVar.get(), self._startVar.get(), self._topleftVar.get(), self._winVar.get())

    def getTurn(self) -> str:
        '''Returns a str for message boxes containing current player's turn'''
        if self._gamestate.getTurn() == othello.WHITE:
            return 'White\'s turn'
        else:
            return 'Black\'s turn'
        
    def _gamestate_check(self) -> None:
        '''Checks whether current player has turns left, and if game is over'''
        check = True
        if self._gamestate.move_check() == 0:
            self._gamestate.switch_turn()
            if self._gamestate.move_check() == 0:
                self._gamestate.GameOver()
                check = False
                
                self._game_result()
        if check:
            self._message_box['text'] = self.getTurn()

    def _game_result(self) -> None:
        '''Display a window with winner's information'''
        self._gameresults = tkinter.Toplevel()
        self._gameresults.title('Results of this round')
        self._gameresults.resizable(0, 0)


 
        if self._gamestate.getWinner() == othello.WHITE:
            message = 'The winner is white player!'
        elif self._gamestate.getWinner() == othello.BLACK:
            message = 'The winner is black player!'
        else:
            message = 'The game was a tie'
            
        self._label = tkinter.Label(master = self._gameresults, text = message, font = ('Helvetica', '14'))
        self._label.grid(row = 0, column = 0, padx = 40, pady = 10, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._message = tkinter.Label(master = self._gameresults, text = '{} discs vs. {} discs'.format(self._gamestate.getWhiteDiscs(), self._gamestate.getBlackDiscs()),
                                           font = ('Helvetica', '14'))
        self._message.grid(row = 2, column = 0, padx = 10, pady = 10)

        self._ok = tkinter.Button(master = self._gameresults, text = 'OK', command = self._end_game, width = 10)
        self._ok.grid(row = 3, column = 0, pady = 20)

        self._gameresults.grab_set()
        self._gameresults.wait_window()

    def _end_game(self) -> None:
        '''Destroys all windows'''
        self._gameresults.destroy()
        self._window.destroy()


    def _set_discs(self) -> None:
        '''Sets the labels for whtie and black discs to correct amount'''
        self._whiteMessage['text'] = '# White discs: {}'.format(self._gamestate.getWhiteDiscs())
        self._blackMessage['text'] = '# Black discs: {}'.format(self._gamestate.getBlackDiscs())

    def _draw_lines(self) -> None:
        '''Draws lines on the canvas'''
        self._draw_columns()
        self._draw_rows()
              
    def _draw_columns(self) -> None:
        '''Draws columns on the canvas'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        self._delta_x = width / self._colVar.get()
        
        for count in range(self._colVar.get()):
            self._canvas.create_line(self._delta_x * count, 0,
                                     self._delta_x * count, height,
                                     fill = 'white')

    def _draw_rows(self) -> None:
        '''Draws rows on the canvas'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        self._delta_y = height / self._rowVar.get()
        
        for count in range(self._rowVar.get()):
            self._canvas.create_line(0, self._delta_y * count,
                                     width, self._delta_y * count,
                                     fill = 'white')

    def _redraw_board(self) -> None:
        '''Redraws the entire board based on updated variables'''
        self._draw_lines()
        self._draw_discs()

    def _canvas_resized(self, event : tkinter.Event) -> None:
        '''Calls listed functions when canvas is resized'''
        self._canvas.delete(tkinter.ALL)
        self._redraw_board()
    

    def _canvas_clicked(self, event : tkinter.Event) -> None:
        '''Calls listed functions when canvas is clicked'''
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        disc = self._find_disc_object(event.x, event.y)
        try:  
            x, y = disc.getFrac()

            self._gamestate.putDisc(disc.getCol() + 1, disc.getRow() + 1)
            
            self._set_discs()
        except othello.DiscPresent: #These 2 exceptions don't need to do anything because GUI message_box
            pass                    #will have the same turn, and user visually will see nothing happened
        except othello.InvalidMove:
            pass
    
        self._redraw_board()
        self._gamestate_check()
          

    def _find_disc_object(self, x : int, y : int) -> disc_model.Disc:
        '''Returns Disc object with x, y, and row, col preset'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        x_pixel, col = self._horizontal_check(x)
        y_pixel, row = self._vertical_check(y)

        disc = disc_model.Disc()
        disc.fromPoint(x_pixel, y_pixel, width, height, col, self._rowVar.get() - row - 1)

        return disc
        

    def _horizontal_check(self, x : int) -> (float, int):
        '''Checks canvas horizontally to find center of mouse click in the cell across horizontal'''
        return self._for_check(x, self._colVar.get(), self._delta_x)

    def _vertical_check(self, y : int) -> (float, int):
        '''Checks canvas vertically to find center of mouse click in the cell across vertical'''
        return self._for_check(y, self._rowVar.get(), self._delta_y)

    def _for_check(self, pixel : int, check_size : int, delta : float) -> (float, int):
        '''Used to find a center of a mouse click among all grid cells'''
        for count in range(check_size):
            if pixel >= delta * count and pixel <= delta * (count + 1):
                return (((delta * count + delta * (count + 1)) / 2), count)

    def _draw_discs(self) -> None:
        '''Draws all the discs in the game logic on the canvas'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        frac_delta_x = self._delta_x / width
        frac_delta_y = self._delta_y / height
        
        for row in range(self._gamestate.getRows()):
            for col in range(self._gamestate.getColumns()):
                if self._gamestate.getBoard()[row][col] == othello.WHITE:
                    disc = disc_model.Disc()
                    disc.fromRowCol(col, row, frac_delta_x, frac_delta_y)
                    self._draw_disc(disc, 'white')
                elif self._gamestate.getBoard()[row][col] == othello.BLACK:
                    disc = disc_model.Disc()
                    disc.fromRowCol(col, row, frac_delta_x, frac_delta_y)
                    self._draw_disc(disc, 'black')
                

    def _draw_disc(self, disc : disc_model.Disc(), color : str) -> None:
        '''Draw a disc on the canvas'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        frac_x, frac_y = disc.getFrac()
        
        self._canvas.create_oval((frac_x - self._x_radius_frac) * width, ((1 - frac_y) - self._y_radius_frac) * height,
                                 (frac_x + self._x_radius_frac) * width, ((1 - frac_y) + self._y_radius_frac) * height,
                                 outline = 'silver', width = 2, fill = color)
        
        



if __name__ == '__main__':
    gameUI = OthelloApplication()
    gameUI.start()

