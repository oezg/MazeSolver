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
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, row, col):
        self._animate()

        # vist the current cell
        self._cells[row][col]._visited = True

        # if we are at the end cell, we are done!
        if row == self._num_cols - 1 and col == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been _visited
        if (
            row > 0
            and not self._cells[row][col]._get_wall("LEFT")
            and not self._cells[row - 1][col]._visited
        ):
            self._cells[row][col].draw_move(self._cells[row - 1][col])
            if self._solve_r(row - 1, col):
                return True
            else:
                self._cells[row][col].draw_move(self._cells[row - 1][col], True)

        # move right if there is no wall and it hasn't been _visited
        if (
            row < self._num_cols - 1
            and not self._cells[row][col]._get_wall("RIGHT")
            and not self._cells[row + 1][col]._visited
        ):
            self._cells[row][col].draw_move(self._cells[row + 1][col])
            if self._solve_r(row + 1, col):
                return True
            else:
                self._cells[row][col].draw_move(self._cells[row + 1][col], True)

        # move up if there is no wall and it hasn't been _visited
        if (
            col > 0
            and not self._cells[row][col]._get_wall("TOP")
            and not self._cells[row][col - 1]._visited
        ):
            self._cells[row][col].draw_move(self._cells[row][col - 1])
            if self._solve_r(row, col - 1):
                return True
            else:
                self._cells[row][col].draw_move(self._cells[row][col - 1], True)

        # move down if there is no wall and it hasn't been _visited
        if (
            col < self._num_rows - 1
            and not self._cells[row][col]._get_wall("BOTTOM")
            and not self._cells[row][col + 1]._visited
        ):
            self._cells[row][col].draw_move(self._cells[row][col + 1])
            if self._solve_r(row, col + 1):
                return True
            else:
                self._cells[row][col].draw_move(self._cells[row][col + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
    
    def A_solve_r(self, row, col):
        self._animate()
        try:
            current_cell = self._cells[row][col]
        except:
            return False
        current_cell.mark_visited()

        if row == self._num_rows - 1 and col == self._num_cols - 1:
            return True

        for direction, delta in Cell.WALLS.items():
            try:
                wall_exists = current_cell._get_wall(direction)
                cell_in_direction = self._cells[row + delta[0]][col + delta[1]]
            except (IndexError, KeyError):
                pass
            else:
                if not (wall_exists or cell_in_direction.is_visited()):
                    current_cell.draw_move(cell_in_direction)
                return self._solve_r(row + delta[0], col + delta[1])
                
                
        return False

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.unvisit()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            next_index_list = []

            possible_direction_indexes = 0

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j]._visited:
                next_index_list.append((i - 1, j))
                possible_direction_indexes += 1
            # right
            if i < self._num_rows - 1 and not self._cells[i + 1][j]._visited:
                next_index_list.append((i + 1, j))
                possible_direction_indexes += 1
            # up
            if j > 0 and not self._cells[i][j - 1]._visited:
                next_index_list.append((i, j - 1))
                possible_direction_indexes += 1
            # down
            if j < self._num_cols - 1 and not self._cells[i][j + 1]._visited:
                next_index_list.append((i, j + 1))
                possible_direction_indexes += 1

            # if there is nowhere to go from here
            # just break out
            if possible_direction_indexes == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(possible_direction_indexes)
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j]._set_wall("RIGHT", False) # has_right_wall = False
                self._cells[i + 1][j]._set_wall("LEFT", False) # has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j]._set_wall("LEFT", False) # has_left_wall = False
                self._cells[i - 1][j]._set_wall("RIGHT", False) # has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j]._set_wall("BOTTOM", False) # has_bottom_wall = False
                self._cells[i][j + 1]._set_wall("TOP", False) # has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j]._set_wall("TOP", False) # has_top_wall = False
                self._cells[i][j - 1]._set_wall("BOTOM", False) # has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
            
    # def _break_walls_r(self, row, col):
    #     self._cells[row][col].mark_visited()
    #     while True:
    #         unvisited_neighbors = []
            
    #         for i, j in Cell.WALLS.values():
    #             if abs(row + i) < self._num_rows \
    #                 and abs(col + j) < self._num_cols \
    #                 and self._cells[row + i][col + j].is_not_visited():
    #                 unvisited_neighbors.append((i, j))    

    #         if not unvisited_neighbors:
    #             self._draw_cell(row, col)
    #             return
            
    #         direction = random.randrange(len(unvisited_neighbors))
    #         next_neighbor = unvisited_neighbors[direction]

    #         # self._cells[row][col]._set_wall(Maze.DIRECTIONS[next_neighbor], False)
    #         # me_from_neighbor = tuple([-val for val in next_neighbor])
    #         # neighbor = [x + y for x, y in zip((row, col), me_from_neighbor)]
    #         # self._cells[neighbor[0]][neighbor[1]]._set_wall(Maze.DIRECTIONS[me_from_neighbor], False)



    #         if next_neighbor == (-1, 0):
    #             self._cells[row][col]._set_wall("LEFT", False)
    #             self._cells[row - 1][col]._set_wall("RIGHT", False)
    #         if next_neighbor == (0, 1):
    #             self._cells[row][col]._set_wall("TOP", False)
    #             self._cells[row][col + 1]._set_wall("BOTTOM", False)
    #         if next_neighbor == (1, 0):
    #             self._cells[row][col]._set_wall("RIGHT", False)
    #             self._cells[row + 1][col]._set_wall("LEFT", False)
    #         if next_neighbor == (0, -1):
    #             self._cells[row][col]._set_wall("BOTTOM", False)
    #             self._cells[row][col - 1]._set_wall("TOP", False)
                            
    #         self._break_walls_r(row + next_neighbor[0], col + next_neighbor[1])

    
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

    
        
        