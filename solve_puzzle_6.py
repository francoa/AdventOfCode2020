import unittest
from import_lines import import_data_to_array


class Group:

    def __init__(self):
        self._members = []

    def add_member(self, member):
        self._members.append(member)

    def get_unique_answers(self):
        answers = ""
        for member in self._members:
            for answer in member:
                if answer not in answers:
                    answers = answers + answer
        return len(answers)

    def get_all_answered(self):
        count = 0
        for answer in self._members[0]:
            if all(answer in member for member in self._members):
                count = count + 1
        return count


def process_puzzle_data(file_name):
    data = import_data_to_array(file_name)
    groups = []
    group = Group()
    for group_member in data:
        if not group_member:
            groups.append(group)
            group = Group()
        else:
            group.add_member(group_member)
    groups.append(group)
    return groups


def solve_puzzle_part_1():
    groups = process_puzzle_data("input_puzzle_6")
    sum_of_counts = 0
    for group in groups:
        sum_of_counts = sum_of_counts + group.get_unique_answers()
    print(f"Count: {sum_of_counts}")


def solve_puzzle_part_2():
    groups = process_puzzle_data("input_puzzle_6")
    sum_of_counts = 0
    for group in groups:
        sum_of_counts = sum_of_counts + group.get_all_answered()
    print(f"Count: {sum_of_counts}")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzle6(unittest.TestCase):

    def test_example_part_1(self):
        groups = process_puzzle_data("test_input_puzzle_6")
        sum_of_counts = 0
        for group in groups:
            sum_of_counts = sum_of_counts + group.get_unique_answers()
        self.assertEqual(11, sum_of_counts)

    def test_example_part_2(self):
        groups = process_puzzle_data("test_input_puzzle_6")
        sum_of_counts = 0
        for group in groups:
            sum_of_counts = sum_of_counts + group.get_all_answered()
        self.assertEqual(6, sum_of_counts)
