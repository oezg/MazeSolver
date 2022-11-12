import typing
from line import Line
from point import Point
from window import Window


class Cell:

    WALLS = {"LEFT": (0, -1), "TOP": (1, 0), "RIGHT": (0, 1), "BOTTOM": (-1, 0)}
    
    def __init__(self, win: typing.Union[Window, None]=None) -> None:
        self._walls = {wall: True for wall in Cell.WALLS}
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win
        self._visited = False

    def _get_wall(self, direction):
        return self._walls.get(direction)


    def unvisit(self):
        if self.is_visited:
            self._visited = False

    def is_visited(self):
        return self._visited
    
    def mark_visited(self) -> None:
        self._visited = True

    def is_not_visited(self) -> bool:
        return not self._visited
    
    def _set_wall(self, wall, stand: bool=True) -> None:
        self._walls[wall] = stand
    
    def draw(self, x1, y1, x2, y2) -> None:
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.draw_walls()

    def draw_walls(self):
        for wall in Cell.WALLS:
            self.draw_wall(wall)

    def draw_wall(self, wall) -> None:
        if self._win is None:
            return
        line = self.get_wall_line(wall)
        color ="black" if self._walls[wall] else "light gray"
        self._win.draw_line(line, color)
    
    def get_wall_line(self, wall) -> Line:
        if wall not in Cell.WALLS:
            raise Exception("No wall exists called {}".format(wall))

        if wall == "LEFT":
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        elif wall == "TOP":
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        elif wall == "RIGHT":
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        
        return line
    
    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        if self._win is None:
            return

        color = 'red'
        if undo:
            color = 'gray'

        center_me = self.get_center_point()
        center_to = to_cell.get_center_point()
        line = Line(center_me, center_to)
        self._win.draw_line(line, color)

    def get_center_point(self) -> Point:
        
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)
