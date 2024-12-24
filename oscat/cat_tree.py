import os
import copy
import logging
from abc import abstractmethod
from oscat.setting import CatTreeProperties


class Os:
    sep_b = b'\\'  # Byte separator for backslash
    seps_b = b'\\/'  # Byte separators for backslash and forward slash
    colon_b = b':'  # Byte colon separator
    sep = '\\'  # String separator for backslash
    seps = '\\/'  # String separators for backslash and forward slash
    colon = ':'  # String colon separator
    dat = os.extsep  # The extension separator for files

    # This property returns the alternative separator for paths (like '/' on Windows)
    @property
    def windows_sep(self):
        return os.altsep

    # This property returns the component separator in environmental paths (like ':' in Unix and ';' in Windows)
    @property
    def pathsep(self):
        return os.pathsep

    # This property returns the line separator in text files (like '\n' in Unix and '\r\n' in Windows)
    @property
    def linesep(self):
        return os.linesep

    # This property returns the default search path for executables
    @property
    def defpath(self):
        return os.defpath

    # This property returns the null device path (like '/dev/null')
    @property
    def devnull(self):
        return os.devnull

    # This property returns the appropriate path constructor (either posixpath or ntpath)
    @property
    def path(self):
        return os.path

    # This property returns the name of the operating system ('posix' or 'nt')
    @property
    def name(self):
        return os.name

    # This property returns the current directory ('.')
    @property
    def curdir(self):
        return os.curdir

    # This property returns the parent directory ('..')
    @property
    def pardir(self):
        return os.pardir

    # This method deletes a CatOs based on the OS type.
    # Input: path (string) - The path of the CatOs to be deleted.
    # Output: None (raises NotImplementedError if the OS type is unsupported)
    def unlink(self, path):
        if os.name == 'posix':
            posix.unlink(path)  # Delete using posix unlink method
        elif os.name == 'nt':
            nt.unlink(path)  # Delete using nt unlink method
        else:
            raise NotImplementedError(f"OS type {os.name} not supported.")

    # This method joins given paths into a single complete path.
    # Input: *paths (strings) - Multiple path components to be joined.
    # Output: string - The combined path as a single string.
    def join(self, *paths):
        return self.sep.join(*paths)

    # This method splits a given CatOs path into components using a specified separator. Input: path (string) - The
    # CatOs path to be split; sep (string, optional) - The separator to use (if not provided, uses default
    # separator). Output: list - The components of the CatOs path.
    def split(self, path, sep=None):
        return path.split(sep if sep else self.sep)

    # This method splits the given path (string or bytes) into components based on the appropriate separators for the data type (str or bytes).
    # Input: path (str or bytes) - The path to be split.
    # Output: list - Components of the path based on the detected separator.
    def split_path(self, path: str or bytes):
        if isinstance(path, bytes):
            if self.sep_b in path:
                return self.split(path, self.sep_b)
            elif self.seps_b in path:
                return self.split(path, self.seps)
            elif self.colon_b in path:
                return self.split(path, self.colon_b)
        else:
            if self.sep in path:
                return self.split(path)
            elif self.seps in path:
                return self.split(path, self.seps)
            elif self.colon in path:
                return self.split(path, self.colon)

    @staticmethod
    def path_exists(path):
        """
        Checks whether the given path exists or not.
        Input: path (string) - The path to check.
        Output: bool - True if the path exists, False otherwise.
        """
        return os.path.exists(path)

    @staticmethod
    def is_dir(path):
        """
        Checks whether the given path is a directory.
        Input: path (string) - The path to check.
        Output: bool - True if the path is a directory, False otherwise.
        """
        return os.path.isdir(path)

    @staticmethod
    def is_file(path):
        """
        Checks whether the given path is a CatOs.
        Input: path (string) - The path to check.
        Output: bool - True if the path is a CatOs, False otherwise.
        """
        return os.path.isfile(path)

    @staticmethod
    def work_space_path(path):
        """
        Retrieves the workspace path based on the given absolute path.
        Input: path (string) - The absolute path to the workspace.
        Output: string - The path to the workspace directory.
        """
        absolute_path = path
        absolute_path_list = absolute_path.split(os.path.sep)
        return os.path.sep.join(
            absolute_path_list[:absolute_path_list.index(CatTreeProperties.work_space_name) + 2]) + os.path.sep


class CatTree(Os):
    # Class variables initialization
    this_file_path = None
    absolute_path = None
    install_path = None
    cat_curser = None

    tree = []
    history = []

    def __init__(self):
        """
        Initialize the CurserTree instance, setting up the paths and tree structure.
        """
        self.initial_setup()

    def cls_vars_initializer(self):
        """
        Initializes the class variables related to file paths and install path.
        This method retrieves the current file's name, its absolute path, and sets the installation path.
        Also sets the cat_curser by appending CatTreeProperties.cats_space_name to install path.
        """
        logging.info("Initializing CatTree...")
        self.this_file_path = os.path.basename(__file__)  # Current CatOs name
        self.absolute_path = os.path.abspath(self.this_file_path)  # Absolute path of the current CatOs
        self.install_path = self.work_space_path(self.absolute_path)  # Installation path derived from workspace
        self.cat_curser = self.install_path + CatTreeProperties.cats_space_name  # cat curser path derived from catsSpace
        logging.info(f"Install path set to {self.install_path}")

    def set_cat_space(self, cat_name : str = None, title : str = "cs"):
        """
        Sets the current cat space by creating a new branch with cat_curser.
        """

        self.new_branch(path = self.cat_curser if not cat_name else self.cat_curser + self.sep + cat_name, title=title)


    def cls_structure_initializer(self):
        """
        Initializes the tree structure with the first branch.
        The first branch contains status, curser_items, and target information.
        Also adds the current os_curser to the history.
        """
        first_branch = {
            "status": True,  # Indicates if the current branch is active
            "curser_items": self.set_curser_items(self.install_path),  # List of items in the current path
            "target": self.target_default(self.install_path),  # Target item (last in the split list),
            "title": "is"
        }

        self.tree.append(first_branch)
        self.history.append(self.os_curser)
        logging.info("CatTree initialized successfully.")

    @abstractmethod
    def do_tasks(self):
        """
        An abstract method to be overridden by subclasses for performing specific tasks.
        """
        pass

    def initial_setup(self):
        """
        Calls the methods to initialize class variables and tree structure, then performs tasks.
        """
        self.cls_vars_initializer()
        self.cls_structure_initializer()
        self.do_tasks()

    def branch_serializer(self, **kwargs):
        """
        Validates the structure of a branch to ensure it has the correct keys and types.
        Returns True if the branch is valid, False otherwise.
        """
        logging.debug(f"Serializing branch with kwargs: {kwargs}")
        if self.tree[0].keys() == kwargs.keys():
            return isinstance(kwargs['curser_items'], list) \
                   and isinstance(kwargs['status'], bool) \
                   and isinstance(kwargs['target'], str) \
                   and isinstance(kwargs['title'], str)
        return False

    def set_curser_items(self, path):
        """
        Splits the provided path into its components and returns a list of non-empty items.
        """
        logging.debug(f"Setting curser items for path: {path}")
        return [path for path in self.split(path) if path]

    def target_default(self, path):
        """
        Sets the default target to the last item in the split path components.
        """
        logging.debug(f"Setting default target for path: {path}")
        return self.set_curser_items(path)[-1]

    def get_target_from_path(self, path):
        """
        Returns the default target for the given path.
        """
        logging.debug(f"Getting target from path: {path}")
        return self.target_default(path)

    def main_dirs_list(self, path=None) -> set:
        """
        Lists the main directories at the given path.
        """
        logging.debug(f"Listing main directories for path: {path}")
        return set(os.listdir(path if path else self.os_curser)) - CatTreeProperties.cat_os_main_dirs

    def add_history(self):
        """
        Adds the current branch to the history.
        """
        logging.debug("Adding current branch to history.")
        self.history.append(self.os_curser)

    @property
    def dirs_list(self) -> set:
        """
        Returns the set of main directories.
        """
        logging.debug("Getting directory list.")
        return self.main_dirs_list()

    def os_cursor_restart(self):
        """
        Restarts the OS cursor.
        """
        logging.info("Restarting OS cursor.")
        super(CatTree, self).os_cursor_restart()

    def add_branch(self, **kwargs):
        """
        Adds a new branch to the tree if all necessary keys are present and valid.
        Input: kwargs (dict) - Contains keys 'curser_items', 'status', 'target', and 'title'.
        Output: None. If the conditions are not met, logs an error.
        """
        logging.debug(f"Adding branch with kwargs: {kwargs}")
        if self.branch_serializer(**kwargs):
            self.tree.append(kwargs)  # Append valid branch to the tree
            logging.info("Branch added successfully.")
        else:
            logging.error("Failed to add branch: missing or invalid keys.")

    def set_new_branch_info(self, path, title=None):
        """
        Sets new branch information including status, curser_items, target, and title.
        """
        try:
            curser_items = self.split_path(path)  # Split the provided path into items
            target = curser_items[-1]
            logging.info("Setting new branch info")

        except Exception as e:
            logging.error(f"Cannot set new branch info: {e}")

        else:
            return {
                "status": True,  # Set new branch as active
                "curser_items": curser_items,  # List of items from the split path
                "target": target,  # Set target to the last item,
                "title": title if title else target
            }

    def set_branch(self, path, title=None):
        """
        Sets the current branch based on the inactive status and the provided path split.
        Output: None. It modifies the tree structure by adding a new branch.
        """
        try:
            logging.debug(f"Setting branch for path: {path}")
            self.inactive_branch_status_list()  # Mark the current branch as inactive
            branch = self.set_new_branch_info(path=path, title=title)

        except Exception as e:
            logging.error(f"Error setting branch: {e}, {__file__}")

        else:
            self.add_branch(**branch)  # Add new branch to the tree
            logging.info("Branch set successfully.")

    def new_branch(self, path: str, not_check=True, title=None) -> None:
        """
        Creates a new branch in the tree based on the provided path.
        Input: path (string) - The path for which the branch is created.
               not_check (bool) - If True, branch is created without checking existence.
        Output: None. Creates a branch if conditions are met.
        """
        logging.debug(f"Creating new branch for path: {path}, not_check: {not_check}")
        if not_check:
            self.set_branch(path=path, title=title)  # Set the branch without checks
        elif not not_check and self.path_exists(path):
            self.set_branch(path=path, title=title)  # Set the branch if path exists

    def check_branch_title(self, title):
        """
        Checks if a branch with the given title exists and is inactive.
        Returns the index of the branch if found, otherwise returns None.
        """
        logging.info("Trying to get branch title index")
        for index, branch in enumerate(self.tree):
            if branch['title'] == title:
                if not branch["status"]:
                    return index
                break
        logging.info("No index found for the branch title")
        return None

    def active_branch(self, index: int):
        """
        Activates the branch at the given index and deactivates the current active branch.
        """
        try:
            self.inactive_branch_status_list()
            self.tree[index]["status"] = True
            logging.info(f"Branch {self.target} activated")
            print(self.tree)
            print(self.tree[index])

        except Exception as e:
            logging.error(f"Error activating branch: {e}")

    def files_path_list(self, title):
        """
        Returns a list of file paths and their corresponding notes for the given title.
        """
        logging.debug(f"Getting files path list for title: {title}")
        return [
            (self.cat_curser + key, value) for key, value in CatTreeProperties.space_files[title].items()
        ]

    def set_branch_space(self, space_name: str, title: str):
        """
        Creates a new branch with the given space name and title.
        """
        logging.debug(f"Setting branch space for {space_name} with title {title}")
        self.new_branch(path=self.cat_curser + space_name, title=title)

    def set_space(self, index, space_name: str, title: str):
        """
        Sets the current space by either activating an existing branch or creating a new one.
        """
        if index is not None:
            self.active_branch(index)
        else:
            self.set_branch_space(space_name=space_name, title=title)

    def has_index_title(self, title):
        """
        Checks if there is an index for the given branch title.
        """
        return self.check_branch_title(title=title)

    def os_ccc(self):
        """
        Sets up and activates the ccat space, or creates a new branch if it doesn't exist.
        """
        logging.info("Setting up ccat space.")
        title = "cc"
        index = self.has_index_title(title=title)
        if index is not None:
            self.set_space(
                index=index,
                space_name=CatTreeProperties.ccat_space,
                title=title
            )
        else:
            logging.info("ccat space does not exist, creating a new branch.")

    def os_dcc(self):
        """
        Sets up and activates the dcat space, or creates a new branch if it doesn't exist.
        """
        logging.info("Setting up dcat space.")
        title = "dc"
        index = self.has_index_title(title=title)
        if index is not None:
            self.set_space(
                index=index,
                space_name=CatTreeProperties.dcat_space,
                title=title
            )
        else:
            logging.info("dcat space does not exist, creating a new branch.")

    @property
    def cc_files(self):
        """
        Returns the list of file paths and their corresponding notes for ccat space.
        """
        logging.debug("Getting ccat files path list.")
        return self.files_path_list(title='cc')

    @property
    def dc_files(self):
        """
        Returns the list of file paths and their corresponding notes for dcat space.
        """
        logging.debug("Getting dcat files path list.")
        return self.files_path_list(title='dc')

    # Ensure the class definition ends properly

    @staticmethod
    def get_key_name_list(key: str, curser_list: list) -> list:
        """
        Retrieves a list of values for a given key from a list of dictionaries.
        Input: key (string) - The key for which values are retrieved.
               curser_list (list) - The list of dictionaries to search.
        Output: list - A list of values for the specified key.
        """
        logging.debug(f"Getting key name list for key: {key}")
        return [curser[key] for curser in curser_list]

    @property
    def tree_satus_list(self) -> list:
        """
        Returns a list of status values for each branch in the tree.
        Output: list - List of boolean statuses of the tree branches.
        """
        logging.debug("Getting tree status list.")
        return self.get_key_name_list("status", self.tree)

    def branch_status_list(self, index) -> int:
        """
        Retrieves the index of the active (True) status in the specified branch index.
        Input: index (int) - The index of the branch to check.
        Output: int - The index of the active status (True).
        """
        logging.debug(f"Getting branch status list for index: {index}")
        return self.get_key_name_list("status", self.tree[index]).index(True)

    @property
    def tree_branch_active_index(self) -> int:
        """
        Gets the index of the currently active branch in the tree.
        Output: int - The index of the active branch.
        """
        logging.debug("Getting tree branch active index.")
        return self.tree_satus_list.index(True)

    @property
    def target(self) -> str:
        """
        Retrieves the target item from the currently active branch.
        Output: string - The target item from the active branch.
        """
        logging.debug(f"Getting target from active branch index: {self.tree_branch_active_index}")
        return self.tree[self.tree_branch_active_index]['target']

    @property
    def targets_list(self) -> list:
        """
        Gets the list of items from the currently active branch.
        Output: list - The list of cursor items from the active branch.
        """
        logging.debug(f"Getting targets list from active branch index: {self.tree_branch_active_index}")
        curser_items = self.tree[self.tree_branch_active_index]["curser_items"]
        return curser_items

    @property
    def target_index(self) -> int:
        """
        Retrieves the index of the target item in the list of cursor items.
        Output: int - The index of the current target in the targets list.
        """
        logging.debug(f"Getting target index for target: {self.target}")
        return self.targets_list.index(self.target)

    def inactive_branch_status_list(self):
        """
        Marks the current active branch as inactive.
        Output: None. Modifies the status of the active branch.
        """
        logging.debug(f"Marking branch {self.tree_branch_active_index} as inactive")
        self.tree[self.tree_branch_active_index]["status"] = False

    @property
    def is_curser_valid(self):
        """
        Checks if the current cursor path exists.
        Output: bool - True if the cursor path exists, False otherwise.
        """
        logging.debug(f"Checking if cursor path exists: {self.os_curser}")
        return self.path_exists(self.os_curser)

    def add_to_branch(self, file_or_dir_name: str) -> None:
        """
        Adds a file or directory name to the current branch's cursor items.
        Input: file_or_dir_name (string) - The name to add to the branch.
        Output: None. Modifies the current branch by adding the new name.
        """
        logging.debug(f"Adding {file_or_dir_name} to branch index: {self.tree_branch_active_index}")
        self.tree[self.tree_branch_active_index]['curser_items'].append(file_or_dir_name)

    def set_target(self, file_or_dir_name):
        """
        Sets the target of the current branch to the provided file or directory name.
        Input: file_or_dir_name (string) - The name to set as the target.
        Output: None. Modifies the target of the active branch.
        """
        logging.debug(f"Setting target to {file_or_dir_name} in branch index: {self.tree_branch_active_index}")
        if file_or_dir_name in self.targets_list:
            self.tree[self.tree_branch_active_index]['target'] = file_or_dir_name
        else:
            logging.warning(f"{file_or_dir_name} not found in targets list.")

    @property
    def miss_file(self) -> bool:
        if "." in str(self.targets_list):
            logging.debug("Miss file check: False")
            return False
        logging.debug("Miss file check: True")
        return True

    @property
    def is_file(self) -> bool:
        """Checks if the current cursor points to a file.
        Output: bool - True if it is a file, otherwise False.
        """
        logging.debug(f"Checking if {self.os_curser} is a file.")
        return os.path.isfile(self.os_curser)

    @property
    def is_directory(self) -> bool:
        """Checks if the current cursor points to a directory.
        Output: bool - True if it is a directory, otherwise False.
        """
        logging.debug(f"Checking if {self.os_curser} is a directory.")
        return os.path.isdir(self.os_curser)

    def is_file_format(self, file_or_dir_name):
        logging.debug(f"Checking if {file_or_dir_name} is a file format.")
        return "." in file_or_dir_name

    def attach_cursor(self, file_or_dir_name, not_check=True):
        """
        Attaches a new file or directory name to the current cursor if it does not already exist.
        Input: file_or_dir_name (string) - The name to attach.
               not_check (bool) - If True, attach without checking for validity.
        Output: None. Modifies the current tree structure or logs an error if invalid.
        """
        tree_back_up = copy.deepcopy(self.tree)  # Backup current tree structure
        logging.debug(f"Attaching {file_or_dir_name} to cursor with not_check={not_check}")

        if self.miss_file and file_or_dir_name not in self.targets_list:
            self.add_to_branch(file_or_dir_name)  # Add new name to the current branch
            self.set_target(file_or_dir_name)  # Set the target to this new name

            if not not_check and not self.is_curser_valid:
                logging.error(f"Cursor path invalid: {self.os_curser}")
                self.tree = tree_back_up  # Restore previous tree on error

        elif self.miss_file and file_or_dir_name in self.targets_list:
            self.set_target(file_or_dir_name)

        elif not self.miss_file and self.is_file_format(file_or_dir_name):
            self.back()
            self.new_branch(self.set_abstract_curser(file_or_dir_name))
            if not not_check and not self.is_curser_valid:
                logging.error(f"Cursor path invalid after new branch: {self.os_curser}")
                self.tree = tree_back_up  # Restore previous tree on error

        else:
            self.set_target(file_or_dir_name)  # Set target to the existing file/directory
        self.add_history()
        logging.info(f"Cursor attached to {file_or_dir_name} successfully.")

    def back_history(self):
        logging.debug("Reverting to previous branch in history.")
        if self.tree_branch_active_index:
            self.tree[self.tree_branch_active_index - 1]['status'] = True
            logging.info(f"Branch status reverted to previous branch: {self.tree_branch_active_index - 1}")

    @property
    def os_curser(self):
        """
        Constructs the cursor path as a string from the targets list.
        Output: string - The constructed cursor path.
        """
        cursor_path = self.sep.join(self.targets_list[:self.target_index + 1])
        logging.debug(f"Constructed cursor path: {cursor_path}")
        return cursor_path

    def set_abstract_curser(self, dir_or_file: str) -> str:
        abstract_cursor = self.os_curser + self.sep + dir_or_file
        logging.debug(f"Set abstract cursor: {abstract_cursor}")
        return abstract_cursor

    def set_abstract_cursor_by_args(self, *args) -> str:
        abstract_cursor_args = self.os_curser + self.sep + self.sep.join(*args)
        logging.debug(f"Set abstract cursor by args: {abstract_cursor_args}")
        return abstract_cursor_args

    @property
    def os_curser_split(self) -> list:
        """
        Splits the current cursor path into its components.
        Output: list - The components of the cursor path.
        """
        cursor_split = self.os_curser.split(self.sep)
        logging.debug(f"Split cursor path: {cursor_split}")
        return cursor_split

    @property
    def last_history(self):
        return self.history[-1]

    def forward(self):
        """
        Advances the cursor to the next target in the list if possible.
        Output: None. If at the end, prints a message indicating the end of cursor history.
        """
        logging.debug("Advancing cursor to the next target.")
        if not self.target == self.targets_list[-1]:
            try:
                self.set_target(self.targets_list[self.target_index + 1])  # Advance to next target
                logging.info(f"Cursor advanced to next target: {self.targets_list[self.target_index + 1]}")
            except Exception as e:
                logging.error(f"Cursor advanced to next target: {e}")
                self.new_branch(self.last_history)
                logging.info("for solv this error use from self.history and creat new branch")

        else:
            logging.info("End of cursor history.")  # Indicate end of available targets
            print("end cursor history")

    def back(self, back_counter : int = 0):
        """
        Moves the cursor back to the previous target in the list.
        Output: None. Modifies the current target to the previous one.
        """
        logging.debug("Reverting cursor to the previous target.")
        self.add_history()
        self.set_target(self.os_curser_split[-(2)-(back_counter)])  # Set target to the previous item
        logging.info(f"Cursor reverted to previous target: {self.os_curser_split[-2]}")

    def branch_back(self):
        """
        Moves back to the previous branch, marking the current branch as inactive.
        Output: None. Modifies the status of branches or prints a message if at the first branch.
        """
        logging.debug("Moving back to the previous branch.")
        branch_active = copy.deepcopy(self.tree_branch_active_index)  # Backup active branch index
        logging.info(f"Branch active index backup: {branch_active}")
        print(not self.tree[branch_active] == self.tree[0])  # Log if not on the first branch
        if not self.tree[branch_active] == self.tree[0]:
            self.inactive_branch_status_list()  # Set current branch as inactive
            self.tree[branch_active - 1]['status'] = True  # Mark previous branch as active
            logging.info(f"Previous branch {branch_active - 1} set to active.")
        else:
            logging.info("First branch encountered.")
            print("first branch")  # Indicate there is no branch before the first one

    def title_index(self, title):

        for index, branch in enumerate(self.tree):
            if branch['title'] == title:
                return index

    @property
    def title_list(self):
        return [branch['title'] for branch in self.tree]

    def has_title(self, title):
        return title in self.title_list

    def active_branch_with_title(self, title):
        if self.has_title(title):
            self.active_branch(
                self.title_index(
                    title
                )
            )
        else:
            print("there is not title")
            print(self.tree)
    def branch_forward(self):
        """
        Advances to the next branch, marking the current branch as inactive.
        Output: None. Modifies the status of branches or prints a message if at the last branch.
        """
        logging.debug("Advancing to the next branch.")
        branch_active = self.tree_branch_active_index  # Get the index of the active branch
        if not self.tree[branch_active] == self.tree[-1]:
            self.inactive_branch_status_list()  # Mark current branch as inactive
            self.tree[branch_active + 1]['status'] = True  # Activate the next branch
            logging.info(f"Next branch {branch_active + 1} set to active.")
        else:
            logging.info("End of branches reached.")
            print("end branch")  # Indicate that this is the last branch
