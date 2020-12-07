

def import_data_to_array(file_name):
    data = []
    try:
        with open(file_name, 'r') as input_file:
            line = input_file.readline()
            while line:
                data.append(line.strip("\n"))
                line = input_file.readline()
    except Exception as exc:
        print(f"There was an exception: {exc}")
    return data
