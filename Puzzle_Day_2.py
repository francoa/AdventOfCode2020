passwords = []
try:
    with open('input_puzzle_2', 'r') as input_file:
        line = input_file.readline()
        while line:
            temp = line.split(":")
            password = temp[1].rstrip('\n').strip()
            temp = temp[0].split(" ")
            letter = temp[1]
            minor = int(temp[0].split("-")[0])
            major = int(temp[0].split("-")[1])
            passwords.append((minor,major,letter,password))
            line = input_file.readline()
except Exception as exc:
    print(f"There was an exception: {exc}")

def find_valid_passwords(passwords):
    count = 0
    for password_tuple in passwords:
        minor,major,letter,password = password_tuple
        occurrences = password.count(letter)
        if occurrences >= minor and occurrences <= major:
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

count = find_valid_passwords_2(passwords)
print(f"Results {count}.")
