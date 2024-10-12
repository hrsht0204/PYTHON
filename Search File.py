import os

def search_file(filename, search_path):
    """Search for a file in the specified directory and return its path if found."""
    filename_lower = filename.lower()
    
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == filename_lower:
                return os.path.join(root, file)
    return None

def main():
    # Specify the directory to search (you can modify this to search in a broader location)
    search_path = r"C:\Users\Hari krishan"  # Change this path as needed
    
    while True:
        # Get the file name from the user
        filename = input("Enter file name (or 'e' to exit): ")
        
        # Check for exit condition
        if filename.lower() == 'e':
            print("Exiting the program.")
            break

        # Search for the file
        found_path = search_file(filename, search_path)
        
        if found_path:
            print(f"File found: {found_path}")
            
            # Check if the file is a text file
            if found_path.lower().endswith('.txt'):
                with open(found_path, 'r') as file:
                    content = file.read()
                    print("\nFile Content:\n")
                    print(content)
                
                # Ask the user if they want to open the file in a new window
                open_choice = input("Do you want to open this file in Notepad? (yes/no): ").strip().lower()
                if open_choice in ['yes', 'y']:
                    os.startfile(found_path)
            else:
                print("The file is not a text file, so it won't be displayed.")
                # Optionally, you can add functionality for other file types here.

        else:
            print("File not found. Please check the file name and try again.")

        # Inform the user about the next step
        print("You can search for another file or type 'e' to exit.")

if __name__ == "__main__":
    main()
