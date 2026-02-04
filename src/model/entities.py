from constants import *

class Cell:

    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__marker = MARKER_EMPTY

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_empty(self) -> bool:
        return self.__marker == MARKER_EMPTY

    def set_marker(self, marker: int) -> None:
        if marker != MARKER_ZERO and marker != MARKER_CROSS:
            raise ValueError(f"Not found marker: {marker}")

        self.__marker = marker

    def reset(self) -> None:
        self.__marker = MARKER_EMPTY


class Field:

    __rows: int
    __columns: int
    __cells: list[list[Cell]]

    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns

        self.__cells = []

    def create(self):

        for i in range(0, self.__rows, 1):
            self.__cells.append([])
            for j in range(0, self.__columns, 1):
                cell = Cell(i, j)
                self.__cells[i].append(cell)



    def reset(self):
        for i in range(0, self.__rows, 1):
            for j in range(0, self.__columns, 1):
                self.__cells[i][j].reset()


    def make_move(self):
        pass