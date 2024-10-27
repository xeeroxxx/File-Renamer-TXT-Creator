import os

def rename_and_create_txt(folder_path, new_name):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Sort files to maintain a consistent order
    files.sort()
    
    # Loop through each file in the folder
    for index, file in enumerate(files, start=1):
        # Create the new file name with leading zeroes (e.g., 01, 02, 03)
        new_file_name = f"{new_name}{index:02}"
        
        # Get the file extension of the current file
        file_extension = os.path.splitext(file)[1]
        
        # Construct the new full file name with extension
        new_file_with_extension = f"{new_file_name}{file_extension}"
        
        # Define the full path of the old and new file
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_file_with_extension)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        
        # Create an empty .txt file with the same name as the new file
        txt_file_path = os.path.join(folder_path, f"{new_file_name}.txt")
        open(txt_file_path, 'w').close()

    print("Renaming and .txt file creation complete!")

if __name__ == "__main__":
    # Get the current working directory
    folder_path = os.getcwd()
    
    # Prompt the user to enter a new base name
    new_name = input("Enter the new base name for the files: ")
    
    # Call the function with the current working directory and the entered name
    rename_and_create_txt(folder_path, new_name)
