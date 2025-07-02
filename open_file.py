import os

def update_file_information(file_path, key, value):

    with open(file_path, "r") as file:
        all_lines = file.readlines()

    with open(file_path, "w") as files:
        for line in all_lines:
            if key in line:
                files.write(key + " " + "=" + " " + value + "\n")
            else:
                files.write(line)

file_path = input("Please provide a file path: ")
if not os.path.exists(file_path):
    print("File does not exist. Please check the path.")
    exit()
if not os.path.isfile(file_path):
    print("Provided path is not a file. Please check the path.")
    exit()

file_key = input("Please provide the key: ")
file_value= input("Please provide the value: ")


update_file_information(file_path,file_key,file_value)

