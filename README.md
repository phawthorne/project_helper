# project_helper

A simple module to help manage paths in a research project. Inspired by DrWatson.jl, but currently MUCH simpler. 

Assumes that you want data, results, and workspace folders that can be reached by, e.g., 
`project.data_folder()`, which will return a `pathlib.Path` object pointing to the 
appropriate folder.

This is particularly intended to help with project portability - as long as all project data
and results are contained in the project folder, no absolute paths will be required, and no fussing about relative paths (e.g. number of ".."s needed to get from script to data) is required either.

## Usage
The way I'm using this is to have my project structured like this:
```
project_dir/
    ...
    - src/
        - scripts/
            project.py
            script.py
    ...
```
 where `project.py` looks like:

```python
from pathlib import Path
from project_helper import Project

project = Project(Path.cwd(), "project_dir")
```

and `script.py` contains
```python
from project import project

project.init_project()

save_results(project.results_folder() / "results.csv")
```

Of course, other scripts can also import `project` from `project.py`, so all the scripts have easy access to project folders through the same `Project` object.
