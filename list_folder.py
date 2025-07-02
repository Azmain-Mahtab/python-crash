import os

def list_files_and_folders_in_folder(folder_name):
    try:
        file_list = os.listdir(folder_name)
        return file_list, None
    except FileNotFoundError:
        return None, f"{folder_name} does not exist"
    except PermissionError:
        return None, f"You do not have permission to access {folder_name}"
    

def main():
    folder_paths = input("Enter a list of folders seperated by commas: ").split(",")

    for folder in folder_paths:
        file_list, error_message = list_files_and_folders_in_folder(folder)
        if file_list:
            print(f"================ Listing contents of folder: ======== {folder.strip()}  ================================")
            for file in file_list:
                print("")
                print(file)
        else:
            print("")
            print(f"================ Error in folder: {folder} ================================")
            print(f"Error: {error_message}")
            

if __name__ == "__main__":
    main()

        




'''folders = input("Enter the foldeer name to list sepearated by comma: ").split(",")'''


'''for folder in folders:
    try:
        file_list = os.listdir(folder)
        print(f"================ Listing contents of folder: ======== {folder}  ================================")
        for file in file_list:
            print(file)
    except FileNotFoundError:
        print(f" {folder} path does not exist")
        break
    except PermissionError:
        print(f" You do not have permission for the {folder} folder")'''

    

'''for folder in folders:
    if os.path.exists(folder):
        files = os.listdir(folder)
        print(f"================ Listing contents of folder: ======== {folder}  ================================")
        for file in files:
            print(file)
    else:
        print("==========================================")
        print(f"folder {folder} path does not exist")'''