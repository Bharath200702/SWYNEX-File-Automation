# SWYNEX File Automation

## Project Description
This is a Python automation project that organizes files into folders based on their file extensions.

## Features
- Automatically organizes files by type.
- Creates folders for different file categories.
- Supports images, documents, videos, audio, spreadsheets, and archives.
- Avoids overwriting files with duplicate names.
- Handles file errors.
- Displays the number of files organized.

## Technologies Used
- Python
- pathlib
- shutil
- Exception handling

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Place test files inside the `sample_files` folder.
4. Open the VS Code terminal.
5. Run this command:

   `python organize_files.py`

## Project Structure
- `organize_files.py` — Main automation script.
- `sample_files/` — Folder containing files to organize.
- `README.md` — Project documentation.

## Safety Note
Test the program using sample files or copies. The script moves files into category folders inside `sample_files`.
