import math

class Row:

    def __init__(self, line):
        self._data = line
        self._num_columns = len(self._data)

    def get_position(self, column):
        curr_col = column
        while curr_col >= self._num_columns:
            curr_col = curr_col - self._num_columns
        return self._data[curr_col]

class Tree_Map:

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


entry_map = Tree_Map()
try:
    with open('input_puzzle_3', 'r') as input_file:
        line = input_file.readline()
        while line:
            entry_map.add_row(line.strip('\n'))
            line = input_file.readline()
except Exception as exc:
    print(f"There was an exception: {exc}")

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

result = []
result.append(count_trees(entry_map, 1, 3, 0, 0))
result.append(count_trees(entry_map, 1, 1, 0, 0))
result.append(count_trees(entry_map, 1, 5, 0, 0))
result.append(count_trees(entry_map, 1, 7, 0, 0))
result.append(count_trees(entry_map, 2, 1, 0, 0))

print(f"Results {result}. Multiplication {math.prod(result)}")
