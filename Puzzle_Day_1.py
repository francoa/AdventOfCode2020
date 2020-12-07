import math
import unittest

from import_lines import import_data_to_array


def process_puzzle_data(input_file):
    lines = import_data_to_array(input_file)
    entries = []
    try:
        for line in lines:
            entries.append(int(line))
    except Exception as exc:
        print(f"There was an exception: {exc}")
    return entries


def find_values(entries, index, value_remaining, number_remaining):
    return_value = []

    while index < len(entries):
        current_value = entries[index]

        if current_value < value_remaining and number_remaining > 1:
            return_value = find_values(entries, index + 1, value_remaining - current_value, number_remaining - 1)
            if len(return_value):
                return_value.append(current_value)
                break

        elif current_value == value_remaining and number_remaining == 1:
            return_value.append(current_value)
            break

        index = index + 1

    return return_value


def solve_puzzle_part_1():
    data = process_puzzle_data('input_puzzle_1')
    result = find_values(data, 0, 2020, 2)

    if len(result) == 2:
        print(f"Results {result}. Multiplication: {math.prod(result)}")
    else:
        print("Couldn't find value")


def solve_puzzle_part_2():
    data = process_puzzle_data('input_puzzle_1')
    result = find_values(data, 0, 2020, 3)

    if len(result) == 3:
        print(f"Results {result}. Multiplication: {math.prod(result)}")
    else:
        print("Couldn't find value")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzle1(unittest.TestCase):

    def test_example_part_1(self):
        entries = [1721, 979, 366, 299, 675, 1456]
        result = find_values(entries, 0, 2020, 2)
        self.assertEqual(math.prod(result), 514579)

    def test_example_part_2(self):
        entries = [1721, 979, 366, 299, 675, 1456]
        result = find_values(entries, 0, 2020, 3)
        self.assertEqual(math.prod(result), 241861950)
