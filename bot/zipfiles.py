import os
from os import path
from shutil import make_archive, move, copy2

def zip_folder(course_folder_name, course_id):
    print(f'Zipping folder - {course_folder_name}')

    course_folder_path = (os.path.join("Skillshare", course_folder_name))
    if path.exists(course_folder_path):
        src = path.realpath("Skillshare")
        response = make_archive(
            base_name = str(course_id),
            format = 'zip',
            root_dir = src,
            base_dir = course_folder_name
        )
        print(f'Done making archive.')
        print(f'Moving - {response}')
        resp = move(
            src = response,
            dst = course_folder_path,
            copy_function = copy2
        )
        print(f'Done Moving.')
        return resp