# Sortify

**Sortify** — A lightweight, intelligent folder organizer to clean up your files effortlessly and efficiently.

## Overview

Sortify is a simple command-line tool that automatically sorts files in any folder into neat, categorized subfolders based on file types. Perfect for quickly decluttering messy folders on your desktop or anywhere on your system.

It requires only Python 3 and works across macOS, Linux, and Windows.

## Features

- Auto-categorizes files into folders like **Images**, **Documents**, **Audio**, **Code**, and more  
- Supports organizing any folder by passing the path as an argument  
- Defaults to sorting the current directory if no folder is specified  
- Lightweight with no external dependencies  
- Easy to use from Terminal with clear console output  
- Handles unknown file types by placing them in an `Others` folder



## Installation

1. Ensure you have **Python 3.6+** installed. You can check your version by running:

       python3 --version

2. Clone or download this repository:

       git clone https://github.com/yourusername/sortify.git
       cd sortify

3. No additional packages or dependencies are required.

## Usage

Run the script via terminal with the following pattern:

        python3 organize.py [folder_path]
        
  - If you omit [folder_path], Sortify organizes the current working directory.

## Example workflows

**Organize the current folder:**

        cd /path/to/folder-to-organize
        python3 /path/to/sortify/organize.py

## How It Works

- Scan: The script scans the specified folder for files (ignoring subfolders).
- Categorize: Files are matched to a category based on their file extension.
- Organize: Files are moved into subfolders named after their categories (created if missing).
- Report: Prints a summary of moved files and folder creations.

The script uses standard Python modules (pathlib, shutil) for maximum compatibility.

## Contributing

Contributions are welcome! Feel free to:

- Add support for more file types or categories
- Improve error handling and edge cases
- Write tests or improve documentation
- Suggest features or open issues

Please fork, commit, and open pull requests!

## License

MIT License 



