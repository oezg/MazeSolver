import random
import time
import typing
from cell import Cell
from window import Window


class Maze:

    DIRECTIONS = {val: key for key, val in Cell.WALLS.items()}
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: typing.Union[Window, None] = None,
            seed=None,
        ) -> None:
        if seed is not None:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = self._create_cells()
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _break_walls_r(self, row, col):
        self._cells[row][col].mark_visited()
        while True:
            unvisited_neighbors = []
            
            for i, j in Cell.WALLS.values():
                if abs(row + i) < self._num_rows \
                    and abs(col + j) < self._num_cols \
                    and self._cells[row + i][col + j].is_not_visited():
                    unvisited_neighbors.append((i, j))    

            if not unvisited_neighbors:
                self._draw_cell(row, col)
                return
            
            direction = random.randrange(len(unvisited_neighbors))
            next_neighbor = unvisited_neighbors[direction]

            self._cells[row][col]._set_wall(Maze.DIRECTIONS[next_neighbor], False)
            me_from_neighbor = tuple([-val for val in next_neighbor])
            neighbor = [x + y for x, y in zip((row, col), me_from_neighbor)]
            self._cells[neighbor[0]][neighbor[1]]._set_wall(Maze.DIRECTIONS[me_from_neighbor], False)



            # if next_neighbor == (-1, 0):
            #     self._cells[row][col]._set_wall("LEFT", False)
            #     self._cells[row][col - 1]._set_wall("RIGHT", False)
            # if next_neighbor == (0, 1):
            #     self._cells[row][col]._set_wall("TOP", False)
            #     self._cells[row + 1][col]._set_wall("BOTTOM", False)
            # if next_neighbor == (1, 0):
            #     self._cells[row][col]._set_wall("RIGHT", False)
            #     self._cells[row][col + 1]._set_wall("LEFT", False)
            # if next_neighbor == (0, -1):
            #     self._cells[row][col]._set_wall("BOTTOM", False)
            #     self._cells[row - 1][col]._set_wall("TOP", False)
                            
            self._break_walls_r(neighbor[0], neighbor[1])

    
    def _create_cells(self) -> typing.List[typing.List[Cell]]:
        return [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        
    def _draw_cells(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col)
                
    
    def _draw_cell(self, row, col) -> None:
        if self._win is None:
            return
        x1, y1, x2, y2 =(
            self._x1 + col * self._cell_size_x,
            self._y1 + row * self._cell_size_y,
            self._x1 + (col + 1) * self._cell_size_x,
            self._y1 + (row + 1) * self._cell_size_y,
        )
        self._cells[row][col].draw(x1, y1, x2, y2)
        self._animate()
    
    def _break_entrance_and_exit(self):
        if not self._cells:
            return
        self._cells[0][0]._set_wall("TOP", False)
        self._draw_cell(0, 0)
        self._cells[-1][-1]._set_wall("BOTTOM", False)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    
        
        