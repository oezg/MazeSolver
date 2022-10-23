from tkinter import Tk, BOTH, Canvas

from line import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__width: int = width
        self.__height: int = height
        self.__root: Tk = Tk()
        self.__root.title("Maze Solver")
        self.__canvas: Canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__running: bool = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self) -> None:
        self.running = False

    @property
    def canvas(self) -> Canvas:
        return self.__canvas

    @property
    def width(self) -> int:
        return self.__width
    
    @width.setter
    def width(self, width: int) -> None:
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height
    
    @height.setter
    def height(self, height: int) -> None:
        self.__height = height
    
    @property
    def running(self) -> bool:
        return self.__running
    
    @running.setter
    def running(self, running) -> None:
        self.__running = running

    