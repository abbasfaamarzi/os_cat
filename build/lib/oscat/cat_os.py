import copy
import logging
import os
import shutil  # Importing shutil for CatOs operations

from oscat.cat_tree import CatTree, CatTreeProperties

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

class CatFile(CatTree):

    def cats_area(self):
        self.set_cat_space()
        self.make_dir()

    def set_space_files(self,title : str):
        for key, value in CatTreeProperties.space_files[title].items():
            self.file_customize(
                path= self.os_curser + self.sep + key,
                text= value
            )
    def cc_space(self):
        title = "cc"
        self.set_cat_space(cat_name= CatTreeProperties.ccat_space, title=title)
        self.make_dir()
        self.set_space_files(title=title)

    def dc_space(self):
        title = "dc"
        self.set_cat_space(cat_name= CatTreeProperties.dcat_space, title=title)
        self.make_dir()
        dc_dir = copy.copy(self.os_curser)
        self.set_os_curser("apps")
        self.make_dir()
        self.set_os_curser("admin")
        self.make_dir()
        self.set_space_files(title=title)
        self.new_branch(path=dc_dir, title="dc")
        self.set_os_curser("storage")
        st_dir = copy.copy(self.os_curser)
        self.make_dir()
        self.set_os_curser("videos")
        self.make_dir()
        self.new_branch(path=st_dir, title="st")
        self.set_os_curser("images")
        self.make_dir()
        self.new_branch(path=st_dir, title="st")
        self.set_os_curser("files")
        self.make_dir()

        print(self.os_curser)

    def cat_manager(self):
        """
        Sets up the cat manager file and writes initial content.
        """
        logging.info("Setting cat manager file and creating.")
        self.set_os_curser("manage")
        self.new_file()
        self.write_file(CatTreeProperties.note_book.cat_manage)

    def do_tasks(self):
        """
        Performs a series of tasks: sets cat space, creates directories, and initializes files.
        """
        logging.info("Starting tasks:\n")
        self.cats_area()
        self.cat_manager()
        self.cc_space()
        self.dc_space()

        logging.info("Tasks completed successfully.")

    def set_os_curser(self, attach_name, not_check=True):
        """
        Sets the operating system cursor for CatOs or directory handling.
        Input: attach_name (string) - The name to attach to the cursor.
               not_check (bool) - If True, skips existence checks.
        """
        self.attach_cursor(attach_name, not_check=not_check)

    def make_dir(self, os_curser=None) -> None:
        """
        Creates a directory at the current cursor path if it does not exist.
        Input: os_curser (string) - The path for the directory.
        """
        if not self.path_exists(self.os_curser):
            os.mkdir(self.os_curser if not os_curser else os_curser)
            logging.info(f"Directory created at {self.os_curser if not os_curser else os_curser}")

    def delete(self) -> None:
        """
        Deletes the CatOs or directory pointed to by the cursor.
        """
        if self.is_file:
            try:
                os.remove(self.os_curser)  # Remove CatOs
                logging.info(f"Deleted CatOs: {self.os_curser}")
            except Exception as e:
                logging.error(f"Error deleting CatOs: {e}")
        elif self.is_directory:
            try:
                os.rmdir(self.os_curser)  # Remove empty directory
                logging.info(f"Deleted directory: {self.os_curser}")
            except OSError:
                # Use shutil to remove non-empty directory
                shutil.rmtree(self.os_curser)
                logging.info(f"Non-empty directory '{self.os_curser}' and all its contents deleted.")
            except Exception as e:
                logging.error(f"Error deleting directory: {e}")
        else:
            logging.error(f"Invalid path (not a CatOs or directory): {self.os_curser}")

    @staticmethod
    def file_customize(path, text=None, read=None, file_format: str = "py"):
        """
        Customizes file operations: creates, writes, or reads files.
        Input: path (string) - The file path.
               text (string) - The text to write to the file.
               read (bool) - If True, reads the file content.
               file_format (string) - The file extension.
        """
        with open(f"{path}.{file_format}", "w" if not text and not read else "a" if text and not read else 'r') as f:
            if text and not read:
                f.write(text)
                logging.info(f"Written text to file at {path}.{file_format}")
            elif not text and read:
                logging.info(f"Reading file at {path}.{file_format}")
                return f.read()

    def new_file(self, file_format: str = "py") -> None:
        """
        Creates a new, empty CatOs at the cursor's current path.
        Input: file_format (string) - The file extension.
        """
        self.file_customize(path=self.os_curser, file_format=file_format)

    def write_file(self, text) -> None:
        """
        Writes text to the CatOs at the current cursor path.
        Input: text (string) - The text to write to the CatOs.
        """
        self.file_customize(path=self.os_curser, text=text)

    @property
    def read_file(self) -> str:
        """
        Reads the first line from the CatOs pointed to by the cursor.
        Output: string - The content of the first line of the CatOs.
        """
        return self.file_customize(path=self.os_curser, read=True)

    def copy(self, dest_path: str) -> None:
        """
        Copies the CatOs or directory pointed to by the cursor to the specified destination path.
        Input: dest_path (string) - The destination path where the CatOs or directory will be copied.
        """
        try:
            if self.is_file:
                shutil.copy(self.os_curser, dest_path)  # Copy CatOs
                logging.info(f"Copied CatOs to: {dest_path}")
            elif self.is_directory:
                shutil.copytree(self.os_curser, dest_path)  # Copy directory
                logging.info(f"Copied directory to: {dest_path}")
            else:
                logging.error(f"Invalid path: {self.os_curser} cannot be copied.")
        except Exception as e:
            logging.error(f"Error copying: {e}")

    def rename(self, new_name: str) -> None:
        """
        Renames the CatOs or directory pointed to by the cursor.
        Input: new_name (string) - The new name for the CatOs or directory.
        """
        try:
            new_path = os.path.join(os.path.dirname(self.os_curser), new_name)
            logging.info(f"New path to rename is {new_path}")

        except Exception as e:
            logging.error(f"Error renaming: {e}")
        else:
            if self.path_exists(self.os_curser):
                try:
                    os.rename(self.os_curser, new_path)  # Rename CatOs or directory
                    logging.info(f"Renamed to: {new_path}")
                    self.new_branch(new_name)  # Update cursor to the new name

                except Exception as e:
                    logging.error(f"Can't rename this file/dir because: {e}")
            else:
                logging.error(f"Path does not exist: {self.os_curser}")

    def cut_and_paste(self, dest_path: str) -> None:
        """
        Cuts (moves) the CatOs or directory to the specified destination path.
        Input: dest_path (string) - The destination path where the CatOs or directory will be moved.
        """
        try:
            if self.is_file:
                shutil.move(self.os_curser, dest_path)  # Move CatOs
                logging.info(f"Moved CatOs to: {dest_path}")
            elif self.is_directory:
                shutil.move(self.os_curser, dest_path)  # Move directory
                logging.info(f"Moved directory to: {dest_path}")
            else:
                logging.error(f"Invalid path: {self.os_curser} cannot be moved.")
        except Exception as e:
            logging.error(f"Error moving: {e}")

    @staticmethod
    def transfer(source_path: str, dest_path: str) -> None:
        """
        Transfers a CatOs or directory from source path to destination path.
        Input: source_path (string) - The path of the source CatOs or directory.
               dest_path (string) - The path of the destination CatOs or directory.
        """
        try:
            shutil.move(source_path, dest_path)  # Move from source to destination
            logging.info(f"Transferred from {source_path} to {dest_path}")
        except Exception as e:
            logging.error(f"Error transferring: {e}")

    def trash_file(self):
        """
        Moves deleted files to a designated trash directory (placeholder for future implementation).
        """
        pass  # Implementation for trashing files or directories can be added here
