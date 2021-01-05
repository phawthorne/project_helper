import sys
import inspect
from pathlib import Path


class Project(object):
    """
    This is an object that helps with finding things like data and results folders
    from a source hierarchy and without needing to identify which computer the 
    code is on.
    
    I can't find a way to look up the full path of the calling location, though, so
    for now callers need to put Path.cwd() in calling_path. 
    """
    def __init__(self, calling_path, project_root_name, to_skip=0,
                 results_folder_name="results", data_folder_name="data",
                 workspace_folder_name="workspace"):
        """
        Searches recursively up from calling location to find a folder named
        `project_root_name`. Will skip `skip` number of such folders. 
        """
        # print(inspect.stack())
        # print(inspect.getfile(sys._getframe(1)))
        # print(Path(__file__).resolve())
        # print(Path.cwd())
        
        p = calling_path.resolve()
        l = list(p.parts)
        skipped = 0
        
        while ((last := l.pop()) != project_root_name) or (skipped < to_skip):
            if last == project_root_name:
                skipped = skipped + 1
        
        l.append(project_root_name)
        self._project_root = Path(*l)

    def project_root(self):
        return self._project_root
    
    def results_folder(self):
        return self._project_root / results_folder_name
    
    def workspace_folder(self):
        return self._project_root / workspace_folder_name
    
    def data_folder(self):
        return self._project_root / data_folder_name
    
    def init_project(self):
        folders = [self.results_folder(), self.workspace_folder(), self.data_folder()]
        for folder in folders:
            if not folder.exists():
                folder.mkdir()
    
    
        
