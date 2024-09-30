# File Management Script

This Python script automatically organizes files in the Downloads directory based on their file type. It moves files to appropriate directories such as Documents, Pictures, and extracts archives to a specified location.

## Features

- Moves PDF, DOCX, TXT, XLS, and PPTX files to the Documents directory.
- Moves JPG, PNG, and JPEG files to the Pictures directory.
- Extracts ZIP, TAR, and GZ archives and moves the extracted contents to the Documents directory.
- Removes DMG, EXE, and DS_Store files.
- Renames files if a file with the same name already exists in the destination directory.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:
   ```sh
   python3 script.py
