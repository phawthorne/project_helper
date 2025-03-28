from pathlib import Path


def ensure_folder(folder_path):
    """
    Make folder `folder_path` if it doesn't exist
    
    Parameters:
    -----------
    folder_path : str or Path
        Path to the folder to create
    """
    path = Path(folder_path)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
