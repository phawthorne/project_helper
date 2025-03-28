import sys
import inspect
from pathlib import Path
from .utils import ensure_folder


class Project(object):
    """
    This is an object that helps with finding things like data and results folders
    from a source hierarchy and without needing to identify which computer the 
    code is on.
    """
    def __init__(self, project_root_name,
                 results_folder_name="results",
                 data_folder_name="data",
                 workspace_folder_name="workspace",
                 src_folder_name="src",
                 scripts_folder_name="scripts"):
        """
        Searches recursively up from calling location to find a folder named
        `project_root_name`.
        
        Parameters:
        -----------
        project_root_name : str
            Name of the project root folder to search for
        *_folder_name : str, optional
            Names for the various project folders
        """
        
        self.results_folder_name = results_folder_name
        self.data_folder_name = data_folder_name
        self.workspace_folder_name = workspace_folder_name
        self.src_folder_name = src_folder_name
        self.scripts_folder_name = scripts_folder_name
                
        # Get the path of the file that called this class
        frame = inspect.currentframe()
        calling_path = Path(inspect.getfile(frame.f_back)).resolve()
        p = calling_path.parent
        
        # Walk up directory structure to find project root
        found = False
        while p.parts:
            if p.name == project_root_name:
                found = True
                break
            p = p.parent
            
        if not found:
            raise ValueError(f"Could not find a directory named '{project_root_name}' in the path hierarchy above {calling_path}")
        
        self._project_root = p
        
        self.project_root = self._project_root
        self.results_folder = self._project_root.joinpath(self.results_folder_name)
        self.data_folder = self._project_root.joinpath(self.data_folder_name)
        self.workspace_folder = self._project_root.joinpath(self.workspace_folder_name)
        self.src_folder = self._project_root.joinpath(self.src_folder_name)
        self.scripts_folder = self._project_root.joinpath(self.scripts_folder_name)
        
    
    def init_project(self):
        """
        Initialize the project structure by creating all standard folders
        and adding the src folder to the Python path.
        """
        folders = [self.results_folder, self.workspace_folder, self.data_folder,
                   self.src_folder, self.scripts_folder]
        for folder in folders:
            ensure_folder(folder)
        
        if str(self.src_folder) not in sys.path:
            sys.path.append(str(self.src_folder))



