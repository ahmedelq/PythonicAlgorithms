# coding: utf-8
""" 
Short script for file management automation. 
"""
__author__ = "https://www.github.com/ahmedelq"

import os
import pathlib
import datetime
import sys

def get_files(dir="."):
    """ Gets all the files recursivly from a given base directory.


    Args: 
        dir (str): The base directory path.
    

    Returns: 
        list: A list that contains all files. 
    """
    folder_queue = [dir]
    files = set()
    while(folder_queue):
        next_folder = folder_queue.pop(0)
        with os.scandir(next_folder) as it:
            for entry in it:
                    if entry.is_file():
                        files.add(entry)
                    else:
                        folder_queue.append(entry.path)
    files = list(files)
    return files


def sort(files, d_path):
    """ Moves files to new directories based on its timestamp. 


    Args: 
        files (list): List of file paths. 
    
    Returns:
        tuple: number of moved files successfully, and number of failed moves. 
    """
    file_ext = lambda x: os.path.splitext(x)[1].replace('.', '') or 'etc'
    n_moved = 0
    for file in files:
        try:
            f_stat = file.stat()
            f_timestamp = abs(min(f_stat.st_mtime, f_stat.st_ctime))
            f_date = datetime.datetime.fromtimestamp(f_timestamp)
            ext = file_ext(file.name)
            new_folder = f'{d_path}\\{f_date.year}\\{f_date.month}\\{ext}'
            new_file_path =  new_folder + f'\\{file.name}'
            os.makedirs(new_folder, exist_ok=True)
            os.rename(file.path, new_file_path)
            n_moved += 1
        except FileExistsError:
            print('[❌]', file.path)
            continue
    return (n_moved, len(files) - n_moved)

if __name__ == "__main__":
    if len(sys.argv) < 3:
       f_path = input("Directory path: ")
       d_path = input("Destination path: ")
    else:
        f_path = sys.argv[1]
        d_path = sys.argv[2]

    if not all( [os.path.exists(f_path), os.path.isdir(f_path)] ):
        exit("Invalid directory path.")
    

    print('Sorting started')
    files = get_files(f_path)
    n, m = sort(files, d_path)
    print('Sorted {:,} files. {:,} remaining.   '.format(n, m))

