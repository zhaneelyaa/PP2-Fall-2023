import os
def delete_file(file_path):
   if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            except Exception as e:
                print(f"Error deleting file '{file_path}': {e}")
        else:
            print(f"Permission denied: You don't have the necessary write permissions for '{file_path}'.")
    else:
        print(f"File '{file_path}' not found.")

file_path_to_delete = "/path/to/your/file.txt"
delete_file(file_path_to_delete)
