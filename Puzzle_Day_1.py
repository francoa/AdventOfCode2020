import math

entries = []
try:
    with open('input_puzzle_1', 'r') as input_file:
        number = input_file.readline()
        while number:
            entries.append(int(number))
            number = input_file.readline()
except Exception as exc:
    print(f"There was an exception: {exc}")

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


number_of_values_to_find = 3 
result = find_values(entries, 0, 2020, number_of_values_to_find)

if len(result) == number_of_values_to_find:
    print(f"Results {result}. Multiplication: {math.prod(result)}")
else:
    print("Couldn't find value")
