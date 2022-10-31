import time
from cell import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for j in range(self._num_cols):
            column = []
            for i in range(self._num_rows):
                cell = Cell(
                    self._x1 + j * self._cell_size_x,
                    self._y1 + i * self._cell_size_y,
                    self._x1 + (j + 1) * self._cell_size_x,
                    self._y1 + (i + 1) * self._cell_size_y,
                    self._win,
                )
                column.append(cell)
            self._cells.append(column)
        for column in self._cells:
            for cell in column:
                cell.draw()
                self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

        
        
        