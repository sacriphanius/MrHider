import os

def hide(file_path, target_file_path):
    with open(file_path, 'rb') as file_to_hide:
        hidden_data = file_to_hide.read()

    with open(target_file_path, 'ab') as target_file:
        target_file.write(hidden_data)

def extract(target_file_path, extracted_file_path):
    with open(target_file_path, 'rb') as target_file:
        hidden_data = target_file.read()

    with open(extracted_file_path, 'wb') as extracted_file:
        extracted_file.write(hidden_data)

def main():
    print("1. Hide\n2. Extract")
    choice = input("Choose the operation you want to perform (1/2): ")

    if choice == '1':
        file_path = input("Enter the path of the file you want to hide: ")
        target_file_path = input("Enter the path of the target file where you want to hide the data: ")
        try:
            hide(file_path, target_file_path)
            print("File successfully hidden.")
        except FileNotFoundError:
            print("File not found. Please check the file path.")
    elif choice == '2':
        target_file_path = input("Enter the path of the target file you want to extract from: ")
        if os.path.isfile(target_file_path):  # Is the specified path a file?
            extracted_file_path = input("Enter the path and name to save the extracted file: ")
            try:
                extract(target_file_path, extracted_file_path)
                print("Data successfully extracted.")
            except FileNotFoundError:
                print("Target file not found. Please check the file path.")
        else:
            print("The specified path is not a file. Please enter a file path.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
