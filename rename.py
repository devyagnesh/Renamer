import os

# Function to change the file extension
def change_extension(filename, new_extension):
    base_name, _ = os.path.splitext(filename)
    new_filename = f"{base_name}.{new_extension}"
    return new_filename

# Ask the user for the directory path and new extension
directory_path = input("Enter the directory path where the files are located: ")
new_extension = input("Enter the new extension (without the dot): ")

# Check if the directory exists
if os.path.isdir(directory_path):
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            new_filename = change_extension(file_path, new_extension)
            
            # Rename the file
            try:
                os.rename(file_path, new_filename)
                print(f"File '{filename}' renamed to {new_filename}")
            except Exception as e:
                print(f"An error occurred while renaming '{filename}': {e}")
else:
    print(f"The directory '{directory_path}' does not exist.")
