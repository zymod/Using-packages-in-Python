In this example I will show way to import packages in two ways.

Import by adding a library that includes other packages to sys.path.
This gives us the ability to skip the custom_packages directory in the import which is shown in the main.py file.
- from communication.comm import host

Import by including the full path to the module file from the current directory.
- from custom_packages.communication.comm import host
