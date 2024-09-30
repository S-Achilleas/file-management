import os 
import shutil

files = os.listdir('/Users/axilleas/Downloads')
for file in files:
    if file.endswith('.pdf') or  file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xls') or file.endswith('.pptx'):
        shutil.move(f'/Users/axilleas/Downloads/{file}', '/Users/axilleas/Documents')
    elif file.endswith('.jpg') or  file.endswith('.png') or file.endswith('.jpeg'):
        shutil.move(f'/Users/axilleas/Downloads/{file}', '/Users/axilleas/Pictures')
    elif file.endswith('.zip') or file.endswith('.tar') or file.endswith('.gz'):
        shutil.unpack_archive(f'/Users/axilleas/Downloads/{file}', f'/Users/axilleas/Downloads/{file}:unzipped')
        shutil.rmtree(f'/Users/axilleas/Downloads/{file}')
        shutil.move(f'/Users/axilleas/Downloads/{file}:unzipped', '/Users/axilleas/Documents')
    elif file.endswith('.dmg') or file.endswith('.exe'):
        shutil.rmtree(f'/Users/axilleas/Downloads/{file}')