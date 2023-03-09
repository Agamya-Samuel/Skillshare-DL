import os

from script.skillshare_rss import organise_course_urls

from bot import (DL_LINKS_MASTER_MONGODB_URL, DL_LINKS_MASTER_MONGODB_DATABASE_NAME, DL_LINKS_MASTER_MONGODB_COLLECTION_NAME)
from bot.skillshare_with_classes import Skillshare
from bot.db_handler import (is_duplicate, connect_db, find_document, insert_document)
from bot.zipfiles import zip_folder
from bot.upload_data import upload_file
from bot.delete_data import delete

from script import SKILLSHARE_COOKIE

last_course_id = dict()

def run_rss():
    global last_course_id 
    last_course_id = {
        'POPULAR_CLASSES': '',
        'TRENDING_CLASSES': ''
        }
    
    course_urls, last_course_id = organise_course_urls(number=2, last_course_id=last_course_id)
    for course_url in course_urls:
        manage_task(course_url=course_url)
        
def manage_task(course_url):
    download_instance = Skillshare.initialise(SKILLSHARE_COOKIE=SKILLSHARE_COOKIE, course_url=course_url, from_user_id='bot_rss')
    print(f'{download_instance.__dict__}')
    
    # check duplicate in dB before downloading
    database = connect_db(
        db_url=DL_LINKS_MASTER_MONGODB_URL,
        db_name=DL_LINKS_MASTER_MONGODB_DATABASE_NAME,
        db_collection_name=DL_LINKS_MASTER_MONGODB_COLLECTION_NAME
        )
    collctn = database['collection']
    is_duplicate_resp = is_duplicate(
        id = download_instance.course_id,
        collection = collctn
    )
    print(f'{is_duplicate_resp = }')
    
    if is_duplicate_resp:
        # IF Course_ID already exists in the DB, just search the ID in DB and return back to the user the Download Links
        cursor = find_document(
            collection = collctn,
            id = download_instance.course_id
            )
        cursor = cursor[0]
        anon_url = cursor['anon']
        pd_url = cursor['pd']
        return [anon_url, pd_url]
    
    # IF Course_ID not found in the DB, Download the course
    download_instance.start_download()

    # Zips the course Folder
    zipped_file_path = zip_folder(
        course_folder_name = download_instance.title,
        course_id = download_instance.course_id
        )
    print(f'{zipped_file_path = }')

    # Uploads the .Zip to respective File Servers
    anon_url, pd_url = upload_file(fpath=zipped_file_path)

    # Deletes .Zip file and Course Folder from Local Disk
    delete(folder_path=download_instance.download_path)

    # Add the Downloaded Links to the DB
    insert_document(
        collection = collctn,
        id = download_instance.course_id,
        url = download_instance.course_url,
        name = download_instance.title,
        user = download_instance.from_user_id,
        anon = anon_url,
        pd = pd_url
        )

run_rss()
print(last_course_id)
