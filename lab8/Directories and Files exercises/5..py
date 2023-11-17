def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")

file_path = "/path/to/your/list.txt"
my_list = [1, 2, 3, 4, 5]

write_list_to_file(file_path, my_list)
