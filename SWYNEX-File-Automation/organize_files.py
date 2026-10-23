
from pathlib import Path
import shutil

# Folder containing the files to organize
SOURCE_FOLDER = Path(__file__).parent / "sample_files"

# File extensions and their categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(file_path):
    """Find the category of a file by its extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other Files"


def organize_files():
    """Move files into folders according to their types."""
    if not SOURCE_FOLDER.exists():
        print("Error: sample_files folder was not found.")
        return

    moved_count = 0

    for file_path in SOURCE_FOLDER.iterdir():
        if not file_path.is_file():
            continue

        category = get_category(file_path)
        destination_folder = SOURCE_FOLDER / category

        try:
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file_path.name

            # Avoid overwriting a file with the same name.
            if destination.exists():
                print(f"Skipped duplicate file: {file_path.name}")
                continue

            shutil.move(str(file_path), str(destination))
            print(f"Organized: {file_path.name} -> {category}")
            moved_count += 1

        except OSError as error:
            print(f"Could not process {file_path.name}: {error}")

    print(f"\nAutomation completed! Files organized: {moved_count}")


if __name__ == "__main__":
    try:
        organize_files()
    except KeyboardInterrupt:
        print("\nAutomation stopped by the user.")
