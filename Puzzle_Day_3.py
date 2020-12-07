import math
import unittest
from import_lines import import_data_to_array


def process_puzzle_data(input_file):
    lines = import_data_to_array(input_file)
    entry_map = TreeMap()
    for line in lines:
        entry_map.add_row(line)
    return entry_map


class Row:

    def __init__(self, line):
        self._data = line
        self._num_columns = len(self._data)

    def get_position(self, column):
        curr_col = column
        while curr_col >= self._num_columns:
            curr_col = curr_col - self._num_columns
        return self._data[curr_col]


class TreeMap:

    def __init__(self):
        self._rows = []
        self._num_rows = 0

    def add_row(self, line):
        self._rows.append(Row(line))
        self._num_rows = self._num_rows + 1

    def get_position(self, row, column):
        if row >= self._num_rows:
            raise Exception("Incorrect row index")
        return self._rows[row].get_position(column)


def count_trees(entry_map, slope_rows, slope_columns, start_row, start_column):
    count = 0
    current_row = start_row
    current_col = start_column
    try:
        while 1:
            if entry_map.get_position(current_row, current_col) == '#':
                count = count + 1
            current_row = current_row + slope_rows
            current_col = current_col + slope_columns
    except Exception as exc:
        print(exc)
    return count


def solve_puzzle_part_1():
    entry_map = process_puzzle_data('input_puzzle_3')
    result = count_trees(entry_map, 1, 3, 0, 0)
    print(f"Result {result}.")


def solve_puzzle_part_2():
    entry_map = process_puzzle_data('input_puzzle_3')
    result = []
    result.append(count_trees(entry_map, 1, 3, 0, 0))
    result.append(count_trees(entry_map, 1, 1, 0, 0))
    result.append(count_trees(entry_map, 1, 5, 0, 0))
    result.append(count_trees(entry_map, 1, 7, 0, 0))
    result.append(count_trees(entry_map, 2, 1, 0, 0))
    print(f"Results {result}. Multiplication {math.prod(result)}")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzle3(unittest.TestCase):

    def test_example_part_1(self):
        entry_map = process_puzzle_data('test_input_puzzle_3')
        result = count_trees(entry_map, 1, 3, 0, 0)
        self.assertEqual(7, result)

    def test_example_part_2(self):
        entry_map = process_puzzle_data('test_input_puzzle_3')
        result = []
        result.append(count_trees(entry_map, 1, 3, 0, 0))
        result.append(count_trees(entry_map, 1, 1, 0, 0))
        result.append(count_trees(entry_map, 1, 5, 0, 0))
        result.append(count_trees(entry_map, 1, 7, 0, 0))
        result.append(count_trees(entry_map, 2, 1, 0, 0))
        self.assertEqual(336, math.prod(result))
