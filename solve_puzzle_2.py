import unittest
from import_lines import import_data_to_array


def process_puzzle_data(input_file):
    passwords = []
    lines = import_data_to_array(input_file)
    try:
        for line in lines:
            temp = line.split(":")
            password = temp[1].strip()
            temp = temp[0].split(" ")
            letter = temp[1]
            minor = int(temp[0].split("-")[0])
            major = int(temp[0].split("-")[1])
            passwords.append((minor, major, letter, password))
    except Exception as exc:
        print(f"There was an exception: {exc}")
    return passwords


def find_valid_passwords(passwords):
    count = 0
    for password_tuple in passwords:
        minor, major, letter, password = password_tuple
        occurrences = password.count(letter)
        if minor <= occurrences <= major:
            count = count + 1
    return count


def find_valid_passwords_2(passwords):
    count = 0
    for password_tuple in passwords:
        first, second, letter, password = password_tuple
        coincidences = 1 if password[first-1] == letter else 0
        coincidences = coincidences + 1 if password[second-1] == letter else coincidences
        if coincidences == 1:
            count = count + 1
    return count


def solve_puzzle_part_1():
    password_list = process_puzzle_data('input_puzzle_2')
    result = find_valid_passwords(password_list)
    print(f"Results {result}.")


def solve_puzzle_part_2():
    password_list = process_puzzle_data('input_puzzle_2')
    result = find_valid_passwords_2(password_list)
    print(f"Results {result}.")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzle2(unittest.TestCase):

    def test_example_part_1(self):
        entries = [
            (1, 3, 'a', 'abcde'),
            (1, 3, 'b', 'cdefg'),
            (2, 9, 'c', 'ccccccccc')]
        self.assertEqual(2, find_valid_passwords(entries))

    def test_example_part_2(self):
        entries = [
            (1, 3, 'a', 'abcde'),
            (1, 3, 'b', 'cdefg'),
            (2, 9, 'c', 'ccccccccc')]
        self.assertEqual(1, find_valid_passwords_2(entries))
