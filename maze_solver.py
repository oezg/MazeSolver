from cell import Cell
from line import Line
from point import Point
from window import Window

def main():
    window = Window(800, 600)
    
    cell1 = Cell(10,10, 60,60, window)
    cell2 = Cell(60,10, 120,60, window)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)

    
    
    window.wait_for_close()


if __name__ == "__main__":
    main()