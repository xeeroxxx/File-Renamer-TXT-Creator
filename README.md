# File Renamer & TXT Creator

## Overview
A Python script to rename files in bulk within a specified folder and create corresponding empty `.txt` files.

## Features
- Renames all files in a folder with a user-defined base name and incremental numbering.
- Generates empty `.txt` files matching the renamed files.
- Works with any file extension.

## Installation
### Prerequisites
- Python 3.x installed on your system

### Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/yourxeeroxxx/file-renamer-txt-creator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd file-renamer-txt-creator
    ```

## How to Use
1. Run the script in the folder where the files are located:
    ```bash
    python rename_and_create_txt.py
    ```
2. Enter the new base name when prompted (e.g., entering `File` renames files to `File01`, `File02`, etc.).

## Example
Initial files:

image1.jpg, image2.png, document.pdf

After running the script with base name `File`:

File01.jpg, File02.png, File03.pdf, File01.txt, File02.txt, File03.txt
