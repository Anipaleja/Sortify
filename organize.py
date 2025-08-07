#!/usr/bin/env python3

import argparse
import os
import shutil
from pathlib import Path
from collections import defaultdict

# File categories and their corresponding extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv", ".md"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Audio": [".mp3", ".wav", ".m4a", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".swift"],
    "Executables": [".exe", ".app", ".sh"],
    "Dev Files": [".stl" , ".json", ".xml", ".yaml", ".log", ".md5", ".sha256"]
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    folder = Path(folder_path).resolve()
    
    if not folder.exists() or not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        return

    print(f"Organizing files in: {folder}\n")

    moved_files = defaultdict(list)

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix
            category = get_category(ext)
            destination = folder / category
            destination.mkdir(exist_ok=True)

            try:
                shutil.move(str(file), destination / file.name)
                moved_files[category].append(file.name)
                print(f"Moved: {file.name} ➜ {category}/")
            except Exception as e:
                print(f"Failed to move {file.name}: {e}")

    print("\nOrganizing complete!")
    for category, files in moved_files.items():
        print(f"{category}: {len(files)} file(s)")

def main():
    parser = argparse.ArgumentParser(description="Smart Folder Organizer")
    parser.add_argument("folder", nargs="?", default=os.getcwd(), help="Folder to organize (defaults to current directory)")
    args = parser.parse_args()

    organize_folder(args.folder)

if __name__ == "__main__":
    main()
