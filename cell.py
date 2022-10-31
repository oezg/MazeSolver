from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, x1, y1, x2, y2, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self) -> None:
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        
    def draw_move(self, to_cell: "Cell", undo=False):
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