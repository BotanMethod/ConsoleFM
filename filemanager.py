import os
import getpass
import subprocess
import cmd
from shutil import rmtree
from time import sleep


class FileManager(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = "Welcome to ConsoleOS's File Manager. Type help or ? to list commands.\n"
        self.prompt = f"{getpass.getuser()}|{os.getcwd()}> "
        
    def do_exit(self, arg):
        'Exits from File Manager'
        return True
    def do_cd(self, path):
        'Moves to the specified directory: cd [path]'
        try:
            os.chdir(path)
            self.prompt = f"{getpass.getuser()}|{os.getcwd()}> "
        except Exception as e:
            print(f"Error: {e}")

    def do_showcon(self, arg):
        "Shows folder's contents"
        print("\n".join(os.listdir(os.getcwd())))

    def do_mkdir(self, dirname):
        'Creates a new directory: create_dir [dir_name]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            print(f"Error: {e}")

    def do_deldir(self, dirname):
        'Deletes directory: delete_dir [dir_name]'
        try:
            rmtree(dirname)
            print(f"Directory '{dirname}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rdir(self, args):
        'Renames the directory: rdir [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"Directory '{old_name}' was renamed to '{new_name}' ")
        except Exception as e:
            print(f'Error: {e}')

    def do_mkfile(self, filename):
        'Creates an empty file: create_file [file_name]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delfile(self, filename):
        'Deletes file: delete_file [file_name]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")

    def do_rnfile(self, args):
        'Renames the file: change_name [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_runpy(self, filename):
        'Runs Python Script files: runpy [file_name]'
        try:
            subprocess.run(['python', filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_run(self, filename):
        'Runs .exe files: run [file_name]'
        try:
            subprocess.run([filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_rfile(self, filename):
        'Reads file: read_file [file_name]'
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Error: {e}")

    def do_wfile(self, args):
        'Writes to file: write_file [file_name] [text]'
        try:
            filename, text = args.split(maxsplit=1)
            with open(filename, 'a') as f:
                f.write(text + '\n')
            print(f"Text was written in file '{filename}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_findf(self, filename):
        'Finds for a file in the current directory: search_file [file_name]'
        found = False
        for root, dirs, files in os.walk(os.getcwd()):
            if filename in files:
                print(f"Found: {os.path.join(root, filename)}")
                found = True
        if not found:
            print("File not found.")

    def do_pardir(self, arg):
        'Moves to the parent directory: parent_dir'
        try:
            os.chdir('..')
            self.prompt = f"ConsoleOS@{getpass.getuser()}: [{os.getcwd()}] # "
        except Exception as e:
            print(f"Error: {e}")
            
if __name__ == '__main__':
    FileManager().cmdloop()