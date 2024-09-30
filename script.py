
import os
import shutil

def move_file(file_path, destination):
    base_name = os.path.basename(file_path)
    dest_path = os.path.join(destination, base_name)
    
    # If the destination path already exists, rename the file
    if os.path.exists(dest_path):
        name, ext = os.path.splitext(base_name)
        counter = 1
        new_name = f"{name}_{counter}{ext}"
        dest_path = os.path.join(destination, new_name)
        while os.path.exists(dest_path):
            counter += 1
            new_name = f"{name}_{counter}{ext}"
            dest_path = os.path.join(destination, new_name)
    
    shutil.move(file_path, dest_path)

files = os.listdir('/Users/axilleas/Downloads')
for file in files:
    file_path = f'/Users/axilleas/Downloads/{file}'
    if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xls') or file.endswith('.pptx'):
        move_file(file_path, '/Users/axilleas/Documents')
    elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        move_file(file_path, '/Users/axilleas/Pictures')
    elif file.endswith('.zip') or file.endswith('.tar') or file.endswith('.gz'):
        extract_to = f'/Users/axilleas/Downloads/{file}_unzipped'
        shutil.unpack_archive(file_path, extract_to)
        os.remove(file_path)
        move_file(extract_to, '/Users/axilleas/Documents')
    elif file.endswith('.dmg') or file.endswith('.exe') or file.endswith('.DS_Store'):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
    else:
        move_file(file_path, '/Users/axilleas/Documents')