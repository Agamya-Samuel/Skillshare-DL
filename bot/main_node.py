from bot import (DL_LINKS_MASTER_MONGODB_URL, DL_LINKS_MASTER_MONGODB_DATABASE_NAME, DL_LINKS_MASTER_MONGODB_COLLECTION_NAME,
QUEUE, SKILLSHARE_COOKIE, is_busy_downloading)

import os
from bot.skillshare_with_classes import Skillshare
from bot.db_handler import (Open_DB_Connection, is_duplicate, insert_document, find_document)
from bot.zipfiles import zip_folder
from bot.upload_data import upload_file

from collections import deque

# @run_infinetly_with_2_minutes_interval(q = QUEUE)
# def download_from_queue(QUEUE = QUEUE):
#     if is_busy_downloading:
#         # if busy downlaoding a course, exit to the add_to_queue function, and then exit as a whole
#         return
    
#     is_busy_downloading = True
#     # Checks in DB if the Course_ID already exists or not
#     with Open_DB_Connection(
#         db_url = DL_LINKS_MASTER_MONGODB_URL,
#         db_name = DL_LINKS_MASTER_MONGODB_DATABASE_NAME,
#         db_collection_name = DL_LINKS_MASTER_MONGODB_COLLECTION_NAME
#         ) as database:
#         course_id = get_course_id(url = url)
#         print(f'{course_id = }')
#         collctn = database['collection']
#         duplicate_resp = is_duplicate(
#             id = course_id,
#             collection = collctn
#             )
#         print(f'{duplicate_resp = }')
        
#         if duplicate_resp:
#             # IF Course_ID already exists in the DB, just search the ID in DB and return back to the user the Download Links
#             cursor = find_document(
#                 collection = collctn,
#                 id = course_id
#                 )
#             cursor = cursor[0]
#             anon_url = cursor['anon']
#             pd_url = cursor['pd']
#             return [anon_url, pd_url]
        

#         # If Course_ID not found in DB, then Download the COURSE and add Links to the DB 

#         # Downloads the course, and saves in a Folder
#         course_folder_path, course_title, teacher_name = download_course_by_class_id(course_id = course_id)
        
        
#         # Zips the course Folder
#         source_folder_path = os.path.join(course_folder_path, teacher_name)
#         zip_fname = zip_folder(
#             course_folder_name = course_title,
#             course_id = course_id
#             )
#         print(f'{zip_fname = }')
#         zip_file_path = os.path.join(course_folder_path, zip_fname)
        

#         # Uploads the .Zip to respective File Servers
#         anon_url, pd_url = upload_file(fpath=zip_file_path)


#         # Deletes .Zip file and Course Folder from Local Disk
#         # delete(folder_path=course_folder_path)


#         # Add the Downloaded Links to the DB
#         insert_document(
#             collection = collctn,
#             id = course_id,
#             url = url,
#             name = course_title,
#             user = user_id,
#             anon = anon_url,
#             pd = pd_url
#             )
        

#         # Returns Download Links to Callback functions
#         return [anon_url, pd_url]


def add_to_queue(course_url: str, from_user_id):
    # Creating tasks Instance to be added in the QUEUE
    task_instance = Skillshare(course_url = course_url, from_user_id = from_user_id, SKILLSHARE_COOKIE=SKILLSHARE_COOKIE)
    print(f'{task_instance.course_url = }')
    task_instance.get_course_id()
    print(f'{task_instance.course_id = }')

    QUEUE.append(task_instance)
    print(f'{QUEUE = }')
    print(task_instance)

    # dont call download_from_queue(), it will run on seperate thread downloading courses, doing its own work


def remove_from_queue():
    pass


def download_node(course_url: str, from_user_id):
    add_to_queue(course_url = course_url, from_user_id = from_user_id)