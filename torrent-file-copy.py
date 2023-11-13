import os
import shutil
import re
import logging
from configparser import ConfigParser

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Constants
INPUT_DIRECTORY = 'D:/Torrents COMPLETE'
OUTPUT_DIRECTORY_BASE = 'D:/'

# Read file types and categories from a configuration file
config = ConfigParser()
config.read('file_types.ini')  # Assuming file_types.ini exists with necessary structure

# Regular expression pattern for TV Shows (e.g., S01E01)
TV_SHOW_PATTERN = re.compile(r'S\d{2}E\d{2}', re.IGNORECASE)

def organize_files(start_path, move_files=True):
    """Organize files into categories based on their extensions.

    Args:
        start_path (str): The directory path to start the organization.
        move_files (bool, optional): Flag to move (True) or copy (False) files. Defaults to True.
    """
    for root, _, files in os.walk(start_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            destination_folder = None

            # Check if the file matches the TV show pattern
            if TV_SHOW_PATTERN.search(file) and config.getboolean('Flags', 'process_tv_shows'):
                destination_folder = 'TV Shows'
            else:
                for section in config.sections():
                    if file_extension in config.get(section, 'extensions').split(','):
                        if config.getboolean('Flags', f'process_{section.lower()}'):
                            destination_folder = section
                            break

            if destination_folder:
                src_file = os.path.join(root, file)
                dst_dir = os.path.join(OUTPUT_DIRECTORY_BASE, destination_folder)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir, exist_ok=True)

                try:
                    if move_files:
                        shutil.move(src_file, dst_dir)
                        logging.info(f"Moved {file} to {dst_dir}")
                    else:
                        shutil.copy(src_file, dst_dir)
                        logging.info(f"Copied {file} to {dst_dir}")
                except Exception as e:
                    logging.error(f"Error moving/copying file {file}: {e}")

# Call the function with move_files set to True or False as needed
organize_files(INPUT_DIRECTORY, move_files=True)
