import math
import unittest
from import_lines import import_data_to_array


class Plane:

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._row_letters = self._get_power_of_two(self._rows)
        self._col_letters = self._get_power_of_two(self._columns)

    @staticmethod
    def _get_power_of_two(number):
        count = 0
        multiply = 1
        while multiply < number:
            multiply = multiply * 2
            count = count + 1
        return count

    @staticmethod
    def _get_int_from_binary(zero, one, string_to_decode):
        binary_number = ""
        for letter in string_to_decode:
            if letter == zero:
                binary_number = binary_number + "0"
            elif letter == one:
                binary_number = binary_number + "1"
            else:
                raise Exception("ERROR")
        try:
            number = int(binary_number, 2)
        except Exception:
            number = None
        return number

    def _get_row_position(self, position):
        return self._get_int_from_binary("F", "B", position)

    def _get_col_position(self, position):
        return self._get_int_from_binary("L", "R", position)

    def get_row_and_column(self, position):
        if len(position) != (self._row_letters + self._col_letters):
            raise Exception("Incorrect number of characters")
        return self._get_row_position(position[0:self._row_letters]), \
               self._get_col_position(position[self._row_letters:self._row_letters+self._col_letters])


def get_seat_ids():
    plane = Plane(rows=128, columns=8)
    seats = import_data_to_array("input_puzzle_5")
    seat_ids = []
    for seat in seats:
        row, column = plane.get_row_and_column(seat)
        seat_ids.append(row * 8 + column)
    return seat_ids


def search_missing_seat(seats):
    seats.sort()
    print(seats)
    #max_seat = seats[-1]
    min_seat = seats[0]
    my_seat = 0
    for index in range(len(seats)):
        if seats[index] > min_seat + index:
            my_seat = seats[index] - 1
            break
    # TODO: Perform binary search instead
    return my_seat


def solve_puzzle_part_1():
    seat_ids = get_seat_ids()
    print(f"Highest seat id is {max(seat_ids)}")


def solve_puzzle_part_2():
    seat_ids = get_seat_ids()
    print(f"My seat id is {search_missing_seat(seat_ids)}")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzleX(unittest.TestCase):

    def test_example_part_1(self):
        plane = Plane(rows=128, columns=8)
        row, column = plane.get_row_and_column("BFFFBBFRRR")
        self.assertEqual(70, row)
        self.assertEqual(7, column)
        row, column = plane.get_row_and_column("FFFBBBFRRR")
        self.assertEqual(14, row)
        self.assertEqual(7, column)
        row, column = plane.get_row_and_column("BBFFBBFRLL")
        self.assertEqual(102, row)
        self.assertEqual(4, column)

