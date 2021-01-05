# project_helper

A simple module to help manage paths in a research project. Inspired by DrWatson.jl, but currently MUCH simpler. 

Assumes that you want data, results, and workspace folders that can be reached by, e.g., 
`project.data_folder()`, which will return a `pathlib.Path` object pointing to the 
appropriate folder.

This is particularly intended to help with project portability - as long as all project data
and results are contained in the project folder, no absolute paths will be required, and no fussing about relative paths (e.g. number of ".."s needed to get from script to data) is required either.