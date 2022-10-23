from line import Line
from point import Point
from window import Window

def main():
    window = Window(800, 600)
    
    window.draw_line(Line(Point(30,40), Point(220, 330)), "cyan")
    
    window.wait_for_close()



if __name__ == "__main__":
    main()