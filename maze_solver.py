from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window

def main():
    window = Window(800, 600)
    
    maze = Maze(55, 55, 6, 8, 22, 22, window)

    
    
    window.wait_for_close()


if __name__ == "__main__":
    main()