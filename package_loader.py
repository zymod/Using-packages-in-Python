#!usr/bin/env python
"""
This module is responsible for adding the directory with custom packages to sys.path.
For this reason we will be able to load all packages from custom_packages directory by loading,
a single package_loader module.
"""
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

path_to_custom_packages = BASE_DIR + "/custom_packages"

# We need additionally to include absolute path to core directory because core contain another package.
path_to_core_package = path_to_custom_packages + "/core"

sys.path.append(path_to_custom_packages)
sys.path.append(path_to_core_package)
