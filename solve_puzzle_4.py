import re
import unittest
from import_lines import import_data_to_array

BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION = "eyr"
HEIGHT = "hgt"
HAIR_COLOR = "hcl"
EYE_COLOR = "ecl"
PASSPORT = "pid"
COUNTRY_ID = "cid"

REQUIRED_FIELDS = [BIRTH_YEAR, ISSUE_YEAR, EXPIRATION, HEIGHT, HAIR_COLOR, EYE_COLOR, PASSPORT]
OPTIONAL_FIELDS = [COUNTRY_ID]

VALID_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class Passport:

    def __init__(self, passport_data):
        self.birth_year = passport_data[BIRTH_YEAR] if BIRTH_YEAR in passport_data else None
        self.issue_year = passport_data[ISSUE_YEAR] if ISSUE_YEAR in passport_data else None
        self.expiration = passport_data[EXPIRATION] if EXPIRATION in passport_data else None
        self.height = passport_data[HEIGHT] if HEIGHT in passport_data else None
        self.hair_color = passport_data[HAIR_COLOR] if HAIR_COLOR in passport_data else None
        self.eye_color = passport_data[EYE_COLOR] if EYE_COLOR in passport_data else None
        self.passport = passport_data[PASSPORT] if PASSPORT in passport_data else None
        self.country = passport_data[COUNTRY_ID] if COUNTRY_ID in passport_data else None
        self.fields = passport_data
        self.validation_functions = [self.validate_birthdate, self.validate_issue_year, self.validate_expiration,
                                     self.validate_height, self.validate_hair_color, self.validate_eye_color,
                                     self.validate_passport]

    def has_all_fields(self):
        if all(field in self.fields for field in REQUIRED_FIELDS):
            return True
        return False

    def is_valid(self):
        if not self.has_all_fields():
            return False
        if all(validate_function() for validate_function in self.validation_functions):
            return True
        return False

    @staticmethod
    def validate_number(to_validate, minor, major):
        try:
            year = int(to_validate)
            if minor <= year <= major:
                return True
        except Exception:
            pass
        return False

    def validate_birthdate(self):
        return self.validate_number(self.fields[BIRTH_YEAR], 1920, 2002)

    def validate_issue_year(self):
        return self.validate_number(self.fields[ISSUE_YEAR], 2010, 2020)

    def validate_expiration(self):
        return self.validate_number(self.fields[EXPIRATION], 2020, 2030)

    def validate_height(self):
        height = self.fields[HEIGHT]
        if re.match("^\d+(cm|in)$", height):
            if "cm" in height:
                return self.validate_number(height.strip("cm"), 150, 193)
            if "in" in height:
                return self.validate_number(height.strip("in"), 59, 76)

    def validate_hair_color(self):
        if re.match("^#([0-9a-f]{6})$", self.fields[HAIR_COLOR]):
            return True
        return False

    def validate_eye_color(self):
        if self.fields[EYE_COLOR] in VALID_COLORS:
            return True
        return False

    def validate_passport(self):
        if re.match("^\d{9}$", self.fields[PASSPORT]):
            return True
        return False


def process_puzzle_data(file_name):
    puzzle_data = []
    lines = import_data_to_array(file_name)
    passport_data = {}
    for line in lines:
        if not line:
            puzzle_data.append(Passport(passport_data))
            passport_data = {}
        else:
            fields = line.split(" ")
            for field_data in fields:
                if ":" in field_data:
                    key_value_data = field_data.split(":")
                    passport_data.update({key_value_data[0]: key_value_data[1]})
    return puzzle_data


def solve_puzzle_part_1():
    passports = process_puzzle_data('input_puzzle_4')
    count = 0
    for passport in passports:
        if passport.has_all_fields():
            count = count + 1
    print(f"{passports[0].fields}")
    print(f"Valid passports {count}")


def solve_puzzle_part_2():
    passports = process_puzzle_data('input_puzzle_4')
    count = 0
    for passport in passports:
        if passport.is_valid():
            count = count + 1
    print(f"{passports[0].fields}")
    print(f"Valid passports {count}")


if __name__ == "__main__":
    solve_puzzle_part_2()


"""  TESTING  """


class TestPuzzle4(unittest.TestCase):

    def test_example_part_1(self):
        passports = process_puzzle_data('test_input_puzzle_4')
        count = 0
        for passport in passports:
            if passport.has_all_fields():
                count = count + 1
        self.assertEqual(2, count)

    def test_example_part_2(self):
        passport = Passport({"pid": "087499704", "eyr": "2030", "iyr": "2012", "cid": "139", "ecl": "grn", "hcl":
                             "#ceb3a1", "hgt": "74in", "byr": "1980"})
        self.assertTrue(passport.is_valid())

