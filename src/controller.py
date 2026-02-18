from __future__ import annotations
from model.entities import Field
from src.model.constants import MARKER_EMPTY


class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def check_win(self, marker) -> bool:
        pass

    def check_draw(self) -> bool:
        pass

    def __check_win_by_row(self, marker) -> bool:
        for i in range(self.__field.get_rows()):
            row_is_winning = True

            for j in range(self.__field.get_columns()):
                current_cell_marker = self.__field.get_cell_marker(i, j)

                if current_cell_marker != marker:
                    row_is_winning = False
                    break

            if row_is_winning:
                return True

        return False

    def __check_win_by_column(self, marker) -> bool:
        for i in range(self.__field.get_columns()):
            column_is_winning = True

            for j in range(self.__field.get_rows()):
                current_cell_marker = self.__field.get_cell_marker(i, j)

                if current_cell_marker != marker:
                    column_is_winning = False
                    break

            if column_is_winning:
                return True

        return False

    def __check_win_by_diagonal(self) -> bool: pass


class Game:

    def __init__(self):
        self.__current_player = MARKER_EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:
        pass

    def make_move(self, x, y) -> None:
        pass

    def finish(self) -> None:
        pass

