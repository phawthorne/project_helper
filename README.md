# project_helper

A simple module to help manage paths in a research project. Inspired by [DrWatson.jl](https://github.com/JuliaDynamics/DrWatson.jl), but much simpler. 

Assumes that you want data, results, scripts, src, and workspace folders that can be reached by, e.g., `project.data_folder`, which will return a `pathlib.Path` object pointing to the appropriate folder.

This is particularly intended to help with project portability - as long as all project data
and results are contained in the project folder, no absolute paths will be required, and no fussing about relative paths (e.g. number of ".."s needed to get from script to data) is required either.

## Usage
The way I'm using this is to have my project structured like this:
```
project_dir/
    - data
    - results
    - scripts/      # specific runs, analyses, etc...
        project.py
        script.py   # imports project from project.py
    - src/          # reused code and packages go in here
        - module_a
        - module_b
    - workspace
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

The function **`project.init_project()`** creates folders `data`, `results`, `scripts`, `src`, and `workspace` if they are missing, and adds `src` to `sys.path` so that the modules in `src` can be imported from the various scripts. 

Of course, other scripts can also import `project` from `project.py`, so all the scripts have easy access to project folders through the same `Project` object.
