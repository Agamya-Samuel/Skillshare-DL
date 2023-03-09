import requests
import json

course_urls_list = list()

def get_course_urls(sorting_type = 'POPULAR_CLASSES', after_course = '', num_of_courses = 1) -> list:
    graphql_api_url = "https://www.skillshare.com/api/graphql"

    str1 = '{\"query\":\"query GetClassesByType {\\n\\tclassListByType'
    str2 = '{\\n\\t\\ttotalCount\\n\\t\\tnodes {\\n\\t\\t\\tid\\n\\t\\t\\turl\\n\\t\\t\\tsku\\n\\t\\t}\\n\\t}'
    str3 = '\\n}\\n\",\"operationName\":\"GetClassesByType\"}'
    sorting_type = sorting_type
    after_course = f'\\\"{after_course}\\\"'
    num_of_courses = num_of_courses

    payload = f'{str1}(type: {sorting_type}, first: {num_of_courses}, after: {after_course}) {str2}{str3}'
    headers = {
        "cookie": "device_session_id=72c162f4-c0d0-4a3d-8225-a08ea273ab20; __cf_bm=9P0NvuAVtR1Qe6NctFHX3s52sfmOyJGy1ON3iptm5GU-1677774812-0-ARMZXH2ezsJtC13i%2FBxtUlW9yy%2Fu7vIKzdXRptFQ3IX9QWhoQY0OXYPOHYHYUq1jHC0UWl3775sAcoVvm2%2B04yTZZQHi2Q1GywcpO2KlASEE; device_session_id=72c162f4-c0d0-4a3d-8225-a08ea273ab20",
        "Content-Type": "application/json"
    }

    response = requests.post(
        url=graphql_api_url,
        data=payload,
        headers=headers
        )

    data_json = json.loads(response.text)
    data_list = data_json['data']['classListByType']['nodes']
    
    return data_list

def organise_course_urls(last_course_id, number = 10):
    num = int(number/2)
    list1 = get_course_urls(sorting_type='POPULAR_CLASSES', after_course=last_course_id['POPULAR_CLASSES'], num_of_courses=num)
    list2 = get_course_urls(sorting_type='TRENDING_CLASSES', after_course=last_course_id['TRENDING_CLASSES'], num_of_courses=num)
    for index, (val1, val2) in enumerate(zip(list1, list2)):
        course_urls_list.append(val1['url'])
        course_urls_list.append(val2['url'])
        if (index == (len(list1)-1)) or (index == (len(list1)-1)):
            last_course_id['POPULAR_CLASSES'] = val1['id']
            last_course_id['TRENDING_CLASSES'] = val2['id']
    
    return course_urls_list, last_course_id