from setuptools import setup, find_packages

packages = find_packages()

setup(
    name = "project_helper",
    packages = packages,
    version = "0.0.1",
    description = "Helper for project paths and some other utilities",
    long_description = "Helper for project paths and some other utilities",
    author = "Peter L Hawthorne",
    url = "https://github.com/phawthorne/project_helper",
    install_requires = ['gdal']
)