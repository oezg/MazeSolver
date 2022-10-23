class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x
    
    @x.setter
    def x(self, x: int) -> None:
        self.__x = x
    
    @property
    def y(self) -> int:
        return self.__y
    
    @y.setter
    def y(self, y: int) -> None:
        self.__y = y

    
    
    
