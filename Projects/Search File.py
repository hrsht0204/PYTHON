import os

def list_directory_contents(current_path):
    """List files and folders in the specified directory."""
    try:
        items = os.listdir(current_path)
        print(f"\nContents of '{os.path.basename(current_path)}':\n")
        for item in items:
            print(item)
        return items
    except Exception as e:
        print(f"Error accessing the directory: {e}")
        return []

def search_folder(folder_name, search_path):
    """Search for a folder in the specified directory and return its path if found."""
    folder_name_lower = folder_name.lower()
    
    for root, dirs, files in os.walk(search_path):
        for dir_name in dirs:
            if dir_name.lower() == folder_name_lower:
                return os.path.join(root, dir_name)
    return None

def search_file(filename, search_path):
    """Search for a file in the specified directory and return its path if found."""
    filename_lower = filename.lower()
    
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == filename_lower:
                return os.path.join(root, file)
    return None

def is_text_file(file_path):
    """Check if a file is a text file by attempting to read a small portion of it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read(512)  # Try reading a small portion
        return True
    except:
        return False

def main():
    # Specify the initial directory to start from (you can modify this)
    base_path = r"C:\Users\Hari krishan"  # Change this path as needed
    current_path = base_path

    while True:
        # Get the folder or file name from the user
        filename = input("\nEnter file or folder name to navigate (or 'back' to go up, 'e' to exit): ").strip()
        
        # Check for exit condition
        if filename.lower() == 'e':
            print("Exiting the program.")
            break
        elif filename.lower() == 'b':
            # Go up one directory level if possible
            parent_path = os.path.dirname(current_path)
            if parent_path and parent_path != current_path:
                previous_dir = os.path.basename(current_path)
                current_path = parent_path
                print(f"Moved up from '{previous_dir}' to '{os.path.basename(current_path)}'.")
                # List contents of the new directory after moving up
                list_directory_contents(current_path)
            else:
                print("You're already at the top-level directory.")
            continue

        # Try to search for the folder or file throughout the base directory
        folder_path = search_folder(filename, base_path)
        file_path = search_file(filename, base_path)

        if folder_path:
            previous_dir = os.path.basename(current_path)
            current_path = folder_path
            print(f"Moved to folder: '{os.path.basename(current_path)}' from '{previous_dir}'.")
            # List contents of the found folder
            list_directory_contents(current_path)
            continue
        elif file_path:
            print(f"File found: '{os.path.basename(file_path)}'")
            
            # Check if the file is a text file
            if is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print("\nFile Content:\n")
                    print(content)
                
                # Ask the user if they want to open the file in a new window
                open_choice = input("Do you want to open this file? (yes/no): ").strip().lower()
                if open_choice in ['yes', 'y']:
                    os.startfile(file_path)
            else:
                # Ask if the user wants to open non-text files like videos or images
                open_choice = input(f"Do you want to open it? (yes/no): ").strip().lower()
                if open_choice in ['yes', 'y']:
                    try:
                        os.startfile(file_path)
                        print(f"Opening '{os.path.basename(file_path)}' with its default application.")
                    except Exception as e:
                        print(f"Error opening file: {e}")
                else:
                    print("File opening cancelled by user.")

        else:
            print("File or folder not found. Please check the name and try again.")

        # Inform the user about the next step
        print("You can search for another file or folder, type 'b' to back, or 'e' to exit.")

if __name__ == "__main__":
    main()
