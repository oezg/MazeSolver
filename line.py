from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2    
        )
        canvas.pack()

    @property
    def point1(self) -> Point:
        return self.__point1
    
    @point1.setter
    def point1(self, point: Point) -> None:
        self.__point1 = point

    @property
    def point2(self) -> Point:
        return self.__point2
    
    @point2.setter
    def point2(self, point: Point) -> None:
        self.__point2 = point

    
