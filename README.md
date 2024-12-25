# OS Cat Library
<link rel="stylesheet" href="oscat/docs/styles.css">


<div class="container">
    <img alt="License" src="oscat/docs/catsbanner-1.png"/>
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

### Introduction to the OCat Library

The OCat library is a powerful tool for managing and manipulating files and directories in Python. This library, utilizing the `CatTree` and `CatFile` classes, provides extensive capabilities for file and directory management. Below are brief descriptions of the important functions within these two classes based on their comments.

---

### Functions of the CatTree Class

- **`__init__`**: Initializes an instance of `CatTree`, setting up the initial paths and tree structure.
- **`cls_vars_initializer`**: Initializes class variables related to file paths and install paths.
- **`set_cat_space`**: Sets the current cat space by creating a new branch with `cat_curser`.
- **`cls_structure_initializer`**: Initializes the tree structure with the first branch.
- **`do_tasks`**: An abstract method to be implemented by subclasses for performing specific tasks.
- **`initial_setup`**: Calls methods to initialize class variables and tree structure, then performs tasks.
- **`branch_serializer`**: Validates the structure of a branch to ensure it has the correct keys and types.
- **`set_curser_items`**: Splits the provided path into components and returns a list of non-empty items.
- **`target_default`**: Sets the default target to the last item in the split path components.
- **`get_target_from_path`**: Returns the default target for the given path.
- **`main_dirs_list`**: Lists the main directories at the given path.
- **`add_history`**: Adds the current branch to the history.
- **`dirs_list`**: Returns the set of main directories.
- **`os_cursor_restart`**: Restarts the OS cursor.
- **`add_branch`**: Adds a new branch to the tree.
- **`set_new_branch_info`**: Sets new branch information including status, cursor items, target, and title.
- **`set_branch`**: Sets the current branch based on inactive status and the provided path.
- **`new_branch`**: Creates a new branch based on the provided path.
- **`check_branch_title`**: Checks if a branch with the given title exists and is inactive.
- **`active_branch`**: Activates the branch at the given index.
- **`files_path_list`**: Returns a list of file paths and their corresponding notes for the given title.
- **`set_branch_space`**: Creates a new branch with the given space name and title.
- **`set_space`**: Sets the current space by either activating an existing branch or creating a new one.
- **`has_index_title`**: Checks if there is an index for the given branch title.
- **`os_ccc`**: Sets up and activates the ccat space or creates a new branch if it doesn't exist.
- **`os_dcc`**: Sets up and activates the dcat space or creates a new branch if it doesn't exist.
- **`cc_files`**: Returns the list of file paths and their corresponding notes for the ccat space.
- **`dc_files`**: Returns the list of file paths and their corresponding notes for the dcat space.

---

### Functions of the CatFile Class

- **`cat_space`**: Sets the cat space and creates the directory.
- **`file_factory`**: Creates files with specified content at the given paths.
- **`make_ccat`**: Creates ccat files using the file factory.
- **`make_dcat`**: Creates dcat files using the file factory.
- **`cat_manager`**: Sets up the cat manager file and writes initial content.
- **`do_tasks`**: Performs a series of tasks: setting cat space, creating directories, and initializing files.
- **`set_os_curser`**: Sets the operating system cursor for managing files or directories.
- **`make_dir`**: Creates a directory at the current cursor path if it does not exist.
- **`delete`**: Deletes the file or directory pointed to by the cursor.
- **`file_customize`**: Customizes file operations: creating, writing, or reading files.
- **`new_file`**: Creates a new, empty file at the cursor's current path.
- **`write_file`**: Writes text to the file at the current cursor path.
- **`read_file`**: Reads the first line from the file pointed to by the cursor.
- **`copy`**: Copies the file or directory pointed to by the cursor to the specified destination path.
- **`rename`**: Renames the file or directory pointed to by the cursor.
- **`cut_and_paste`**: Moves the file or directory to the specified destination path.
- **`transfer`**: Transfers a file or directory from the source path to the destination path.
- **`trash_file`**: Moves deleted files to a designated trash directory (placeholder for future implementation).
