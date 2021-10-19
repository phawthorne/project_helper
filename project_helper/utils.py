import os


def ensure_folder(folder_path):
    """Make folder `folder_path` if it doesn't exist"""
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
