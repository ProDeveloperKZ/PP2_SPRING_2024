#task 1

import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_directories_files = [os.path.join(path, item) for item in os.listdir(path)]
    return directories, files, all_directories_files

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
directories, files, all_items = list_directories_files(path)
print("Directories:", directories)
print("Files:", files)
print("All Directories and Files:", all_items)

#task 2

import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
exists, readable, writable, executable = check_path_access(path)
print("Exists:", exists)
print("Readable:", readable)
print("Writable:", writable)
print("Executable:", executable)

#task 3

import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
def get_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist", None

filename, directory = get_filename_and_directory(path)
print("Filename:", filename)
print("Directory:", directory)

#task 4

import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = "A.txt"
line_count = count_lines_in_file(file_path)
print("Number of lines in the file:", line_count)

#task 5

import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(str(item) + '\n')

file_path = "A.txt"
my_list = [1, 2, 3, 4, 5]
write_list_to_file(file_path, my_list)

#task 6

import os
import string

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        pass  # File created with no content

#task 7
    
import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

source_file = "A.txt"
destination_file = "B.txt"
copy_file_contents(source_file, destination_file)

#task 8

import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def delete_file_by_path(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")


file_to_delete = "Z.txt"
delete_file_by_path(file_to_delete)