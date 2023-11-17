import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("Path does not exist.")

def main():
    path = input("Enter the path: ")
    check_path(path)

if __name__ == "__main__":
    main()
