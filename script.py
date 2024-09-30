
import os
import shutil

# Function to move a file to a destination directory
def move_file(file_path, destination):
    # Extract the base name of the file (e.g., 'example.txt')
    base_name = os.path.basename(file_path)
    # Construct the destination path
    dest_path = os.path.join(destination, base_name)
    
    # If the destination path already exists, rename the file
    if os.path.exists(dest_path):
        # Split the base name into name and extension
        name, ext = os.path.splitext(base_name)
        counter = 1
        # Construct a new name by appending a counter (e.g., 'example_1.txt')
        new_name = f"{name}_{counter}{ext}"
        dest_path = os.path.join(destination, new_name)
        # Increment the counter until a unique name is found
        while os.path.exists(dest_path):
            counter += 1
            new_name = f"{name}_{counter}{ext}"
            dest_path = os.path.join(destination, new_name)
    
    # Move the file to the destination path
    shutil.move(file_path, dest_path)

files = os.listdir('/Users/axilleas/Downloads')
for file in files:
    file_path = f'/Users/axilleas/Downloads/{file}'
    if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xls') or file.endswith('.pptx'):
        move_file(file_path, '/Users/axilleas/Documents')
    elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        move_file(file_path, '/Users/axilleas/Pictures')
    elif file.endswith('.zip') or file.endswith('.tar') or file.endswith('.gz'):
        # Extract the archive to a new directory
        extract_to = f'/Users/axilleas/Downloads/{file}_unzipped'
        shutil.unpack_archive(file_path, extract_to)
        # Remove the original archive file
        os.remove(file_path)
        # Move the extracted directory to the Documents directory
        move_file(extract_to, '/Users/axilleas/Documents')
    elif file.endswith('.dmg') or file.endswith('.exe') or file.endswith('.DS_Store'):
        # If it's a directory, remove it
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        # If it's a file, remove it
        else:
            os.remove(file_path)
    else:
        # Move other files to the Documents directory
        move_file(file_path, '/Users/axilleas/Documents')