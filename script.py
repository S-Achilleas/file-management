import os 
import shutil

files = os.listdir('/Users/axilleas/Downloads')
for file in files:
    if file.endswith('.pdf') or  file.endswith('.docx') or file.endswith('.txt'):
        shutil.move(f'/Users/axilleas/Downloads/{file}', '/Users/axilleas/Documents')
    elif file.endswith('.jpg') or  file.endswith('.png') or file.endswith('.jpeg'):
        shutil.move(f'/Users/axilleas/Downloads/{file}', '/Users/axilleas/Pictures')