#Arman Karabakhtsyan 28152667, Project 5, Lab 2

class Disc:
    def fromPoint(self, x : int, y : int, c_width : int, c_height : int, column : int, row : int) -> None:
        '''Sets fraction units from x, y, and canvas size'''
        self._row = row
        self._column = column

        self._xFrac = x / c_width
        self._yFrac = y / c_height


    def getCol(self) -> int:
        '''Returns disc's column'''
        return self._column

    def getRow(self) -> int:
        '''Returns disc's row'''
        return self._row

    def fromRowCol(self, col : int, row : int, delta_x : int, delta_y : int) -> None:
        '''Sets fraction untis from col,row, and cell width, height'''
        self._row = row
        self._column = col

        self._xFrac = (delta_x / 2) + self._column * delta_x
        self._yFrac = (delta_y / 2) + self._row * delta_y
    
    def getFrac(self) -> int:
        '''Return a tuple with fractional coordinates'''
        return (self._xFrac, self._yFrac)
