import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")

file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)
