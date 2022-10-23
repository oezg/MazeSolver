from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.__root: Tk = Tk()
        self.__root.title("Maze Solver")
        self.canvas: Canvas = Canvas().pack()
        self.running: bool = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self) -> None:
        self.running = False