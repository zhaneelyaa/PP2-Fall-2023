import shutil
def copy_file(source_path, destination_path):
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"File contents copied from '{source_path}' to '{destination_path}' successfully.")
    except Exception as e:
        print(f"Error copying file contents: {e}")

source_file_path = "/path/to/your/source_file.txt"
destination_file_path = "/path/to/your/destination_file.txt"

copy_file(source_file_path, destination_file_path)
