import os 
import shutil

files = os.listdir('/Users/axilleas/Downloads')
for file in files:
    file_path = f'/Users/axilleas/Downloads/{file}'
    if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xls') or file.endswith('.pptx'):
        shutil.move(file_path, '/Users/axilleas/Documents')
    elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        shutil.move(file_path, '/Users/axilleas/Pictures')
    elif file.endswith('.zip') or file.endswith('.tar') or file.endswith('.gz'):
        extract_to = f'/Users/axilleas/Downloads/{file}_unzipped'
        shutil.unpack_archive(file_path, extract_to)
        os.remove(file_path)
        shutil.move(extract_to, '/Users/axilleas/Documents')
    elif file.endswith('.dmg') or file.endswith('.exe') or file.endswith('.DS_Store'):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
    else:
        shutil.move(file_path, '/Users/axilleas/Documents')