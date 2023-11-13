# File Organizer Script - README

## Overview
The File Organizer script is a Python utility designed to automatically organize files into designated directories based on their file types. This script is particularly useful for managing large collections of various file types, such as videos, TV shows, audio files, comics, and documents.

## Features
- **Configurable File Categories:** Organize files based on predefined categories and file extensions.
- **Customizable Actions:** Choose to either move or copy files to their respective directories.
- **TV Show Special Handling:** Special regex pattern matching for TV show files.
- **Logging:** Detailed logging for tracking file movements or copies.

## Requirements
- Python 3.x
- `shutil`, `os`, `re`, `logging`, and `configparser` Python modules. These are standard modules and should be available with Python 3.x.
- A configuration file named `file_types.ini` located in the same directory as the script.

## Setup
1. **Place the Script:**
   Ensure that the script file is placed in a suitable location on your system.

2. **Configure `file_types.ini`:**
   Create a `file_types.ini` file in the same directory as the script with the following structure:

   ```ini
   [Category]
   extensions = .ext1, .ext2

   [Flags]
   process_category = True or False
   ```
   Replace `Category` and `extensions` with the appropriate file categories and extensions.

3. **Adjust Constants:**
   Edit the `INPUT_DIRECTORY` and `OUTPUT_DIRECTORY_BASE` constants in the script to match your desired input and output paths.

## Usage
To run the script, use the following command in your terminal or command prompt:
```bash
python file_organizer.py
```

By default, the script moves files. To copy files instead, modify the `organize_files` function call at the bottom of the script:
```python
organize_files(INPUT_DIRECTORY, move_files=False)
```

## Logging
The script logs all its operations, which can be viewed for monitoring the process. By default, the logging level is set to `INFO`.

## Error Handling
The script includes basic error handling to manage common issues such as file access errors. Errors are logged for review.

## Limitations
- The script currently does not handle nested directories within each category.
- The script operates based on file extensions and does not inspect file content.

## Customization
Users are encouraged to modify and extend the script as needed. Possible customizations include adding more file categories, changing the regex for special file types, or modifying the logging setup.

## Contribution
Contributions to the script are welcome. Please ensure that any pull requests or changes adhere to the existing coding style and add meaningful functionality or fixes.

## License
This script is released under the MIT License. See `LICENSE` file for more details.

---

This README provides a comprehensive guide to setting up and using the File Organizer script. For any further questions or contributions, please reach out to the repository maintainer.
