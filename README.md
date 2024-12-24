# OS Cat Library
<link rel="stylesheet" href="oscat/docs/styles.css">


<div class="container">
    <img alt="License" src="oscat/docs/cat.jpg"/>
    <a href="https://github.com/abbasfaramarzi/ocat" class="github-button" target="_blank">
        <img src="oscat/docs/GitHub-Logo.wine .svg" alt="GitHub Logo" style="width: 40px; height: 40px; margin-right: 5px;"/>
        OCat
    </a>
</div>

## Overview
OCat is a powerful Python library designed to manage and manipulate files and directories efficiently. 
Developed by Abbas Faramarzi Filabadi, this library extends functionalities through `CatFile` and `CatTree` classes.

## Features
- Comprehensive file and directory management
- Branch and path history management
- File operations including create, delete, copy, move, and rename
- Custom file support and format handling

## Examples

### Example 1: Initializing and Setting Up Cat Space
```python
from ocat import CatFile

# Initialize CatFile
cf = CatFile()

# Set up cat space and create directory
cf.cat_space()

print("Current OS Cursor:", cf.os_curser)
```

### Example 2: Creating and Writing to a File
```python
from ocat import CatFile

# Initialize CatFile
cf = CatFile()

# Set OS cursor and create a new file
cf.set_os_curser("example_file")
cf.new_file()
cf.write_file("Hello, OCat!")

print("File created and written successfully!")
```

### Example 3: Managing Directories and Files
```python
from ocat import CatFile

# Initialize CatFile
cf = CatFile()

# Create a new directory
cf.set_os_curser("example_directory")
cf.make_dir()

# Create and write to files within the directory
cf.set_os_curser("example_directory/example_file1")
cf.new_file()
cf.write_file("Content for file 1")

cf.set_os_curser("example_directory/example_file2")
cf.new_file()
cf.write_file("Content for file 2")

print("Directory and files created successfully!")
```

### Example 4: Copying and Moving Files
```python
from ocat import CatFile

# Initialize CatFile
cf = CatFile()

# Set OS cursor and create a new file
cf.set_os_curser("file_to_copy")
cf.new_file()
cf.write_file("This file will be copied")

# Copy the file to a new location
cf.copy("copy_of_file_to_copy")
print("File copied successfully!")

# Move the copied file to another location
cf.cut_and_paste("moved_copy_of_file_to_copy")
print("File moved successfully!")
```

### Example 5: Deleting Files and Directories
```python
from ocat import CatFile

# Initialize CatFile
cf = CatFile()

# Set OS cursor and create a new directory and file
cf.set_os_curser("directory_to_delete")
cf.make_dir()
cf.set_os_curser("directory_to_delete/file_to_delete")
cf.new_file()
cf.write_file("This file will be deleted")

# Delete the file and directory
cf.set_os_curser("directory_to_delete/file_to_delete")
cf.delete()
cf.set_os_curser("directory_to_delete")
cf.delete()
print("File and directory deleted successfully!")
```

## Installation
To install this library, you can use pip:

```sh
pip install os_cat
```

To clone the repository directly from GitHub, you can use:
```sh
git clone https://github.com/abbasfaamarzi/os_cat.git
```

