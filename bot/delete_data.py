import shutil
import os

def delete_file(fpath):
    if fpath is None:
        return
    
    print(f'Deleting file {fpath}')
    try:
        os.remove(fpath)
        print(f"{fpath} removed successfully")
    except OSError as error:
        print(error)
        print("File path can not be removed")

def delete_folder(folder_path):
    if folder_path is None:
        return
    
    print(f'Deleting Folder {folder_path}')
    try:
        shutil.rmtree(folder_path)
        print(f"{folder_path} removed successfully")
    except OSError as error:
        print(error)
        print("File path can not be removed")

def delete(fpath = None, folder_path = None):
    print(f'Deleting...')
    delete_folder(folder_path=folder_path)
    delete_file(fpath=fpath)