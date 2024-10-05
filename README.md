# File Organizer Script

This Python script automates the organization of files from your `Downloads` directory, moving them into appropriate folders based on file type and handling special cases like archive extraction.

## How It Works

- **Move Documents**: Files like `.pdf`, `.docx`, `.txt`, `.xls`, `.pptx` are moved to the `Documents` folder.
- **Move Images**: Files like `.jpg`, `.png`, `.jpeg` are moved to the `Pictures` folder.
- **Extract Archives**: Archive files like `.zip`, `.tar`, `.gz` are extracted and then moved to `Documents`. The original archive is deleted.
- **Delete Unnecessary Files**: Files such as `.dmg`, `.exe`, `.DS_Store` are removed.
- **Other Files**: Files not fitting into the above categories are moved to the `Documents` folder by default.

## Prerequisites

- **Python 3.x**
- Standard Python libraries (`os`, `shutil`)

## Usage Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/S-Achilleas/file-management.git

## 2. Modify the script

Replace all instances of `/YOURPATH/` with the correct paths on your system.

### Example:
```python
files = os.listdir('/YOURPATH/Downloads')
```

Replace `/YOURPATH/Downloads` with your actual `Downloads` directory path, and update the destination paths accordingly:

- `/YOURPATH/Documents`
- `/YOURPATH/Pictures`
- `/YOURPATH/Downloads/{file}_unzipped`

## 3. Run the script

Navigate to the directory where the script is located and execute it:

```bash
python script.py
```

The script will automatically organize the files in your `Downloads` folder based on their types, moving them to the appropriate folders.

### Example Paths

- **Downloads Directory**: `/Users/yourname/Downloads`
- **Documents Directory**: `/Users/yourname/Documents`
- **Pictures Directory**: `/Users/yourname/Pictures`

Make sure to update these paths to reflect your actual directory structure.

## Notes

- If a file with the same name already exists in the destination folder, the script will automatically rename the file by appending a counter (e.g., `example_1.txt`).
- Archive files (`.zip`, `.tar`, `.gz`) are extracted to a new directory, which is then moved to the `Documents` folder. The original archive is deleted after extraction.
- Unwanted files such as `.dmg`, `.exe`, and `.DS_Store` are removed from the `Downloads` directory.

## License

This project is licensed under the MIT License.

