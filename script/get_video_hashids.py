import cloudscraper


course_ids_list = [
				{
					"sku": "1382946907"
				},
				{
					"sku": "1709959838"
				},
				{
					"sku": "783727951"
				},
				{
					"sku": "855847904"
				},
				{
					"sku": "1945270638"
				},
				{
					"sku": "1956917187"
				},
				{
					"sku": "544817332"
				},
				{
					"sku": "1005632159"
				},
				{
					"sku": "1694126289"
				},
				{
					"sku": "1880048778"
				},
				{
					"sku": "1036212713"
				},
				{
					"sku": "927988375"
				},
				{
					"sku": "29609066"
				},
				{
					"sku": "9403043"
				},
				{
					"sku": "928999366"
				},
				{
					"sku": "1758731626"
				},
				{
					"sku": "713232985"
				},
				{
					"sku": "1286465364"
				},
				{
					"sku": "1576657189"
				},
				{
					"sku": "1173817055"
				},
				{
					"sku": "647318269"
				},
				{
					"sku": "1528756653"
				},
				{
					"sku": "1300789570"
				},
				{
					"sku": "1749196794"
				},
				{
					"sku": "1501439636"
				},
				{
					"sku": "595513472"
				},
				{
					"sku": "1616049208"
				},
				{
					"sku": "1494805287"
				},
				{
					"sku": "1222868005"
				},
				{
					"sku": "627711705"
				},
				{
					"sku": "1593386596"
				},
				{
					"sku": "1700815729"
				},
				{
					"sku": "1167445153"
				},
				{
					"sku": "215192441"
				},
				{
					"sku": "1203862507"
				},
				{
					"sku": "1890887486"
				},
				{
					"sku": "1997385358"
				},
				{
					"sku": "831325295"
				},
				{
					"sku": "271123352"
				},
				{
					"sku": "981555191"
				},
				{
					"sku": "491579657"
				},
				{
					"sku": "264474542"
				},
				{
					"sku": "1103032154"
				},
				{
					"sku": "1022927245"
				},
				{
					"sku": "2092866629"
				},
				{
					"sku": "101999210"
				},
				{
					"sku": "1812498839"
				},
				{
					"sku": "2062108553"
				},
				{
					"sku": "873689550"
				},
				{
					"sku": "859732432"
				},
				{
					"sku": "1090598258"
				},
				{
					"sku": "1829131241"
				},
				{
					"sku": "909675491"
				},
				{
					"sku": "292988947"
				},
				{
					"sku": "18265272"
				},
				{
					"sku": "471108128"
				},
				{
					"sku": "568214372"
				},
				{
					"sku": "134302840"
				},
				{
					"sku": "261825422"
				},
				{
					"sku": "1047774555"
				},
				{
					"sku": "410198034"
				},
				{
					"sku": "1280042773"
				},
				{
					"sku": "1442682996"
				},
				{
					"sku": "793570975"
				},
				{
					"sku": "1354813179"
				},
				{
					"sku": "1782083086"
				},
				{
					"sku": "1736034566"
				},
				{
					"sku": "1102190230"
				},
				{
					"sku": "110696175"
				},
				{
					"sku": "165219958"
				},
				{
					"sku": "1371171209"
				},
				{
					"sku": "1661390087"
				},
				{
					"sku": "1582006634"
				},
				{
					"sku": "809592591"
				},
				{
					"sku": "192017526"
				},
				{
					"sku": "1389888344"
				},
				{
					"sku": "2056505682"
				},
				{
					"sku": "2103496100"
				},
				{
					"sku": "778582891"
				},
				{
					"sku": "918195786"
				},
				{
					"sku": "1969286157"
				},
				{
					"sku": "1481601744"
				},
				{
					"sku": "543509240"
				},
				{
					"sku": "1717335224"
				},
				{
					"sku": "1598809277"
				},
				{
					"sku": "1308926806"
				},
				{
					"sku": "1733672496"
				},
				{
					"sku": "1944705585"
				},
				{
					"sku": "671324633"
				},
				{
					"sku": "1186479036"
				},
				{
					"sku": "71395792"
				},
				{
					"sku": "1291243341"
				},
				{
					"sku": "454473819"
				},
				{
					"sku": "1893863428"
				},
				{
					"sku": "1597322804"
				},
				{
					"sku": "120243253"
				},
				{
					"sku": "545225513"
				},
				{
					"sku": "178545663"
				},
				{
					"sku": "1772795845"
				},
				{
					"sku": "947883684"
				}
			]


def fetch_course_data_by_class_id(course_id):
    url = f'https://api.skillshare.com/classes/{course_id}'
    scraper = cloudscraper.create_scraper(
        browser={
            'custom': 'Skillshare/4.1.1; Android 5.1.1',
        },
        delay=10
    )

    print(f'{SKILLSHARE_COOKIE = }')
    res = scraper.get(
        url,
        headers={
        'Accept': 'application/vnd.skillshare.class+json;,version=0.8',
        'User-Agent': 'Skillshare/5.3.0; Android 9.0.1',
        'Host': 'api.skillshare.com',
        'Referer': 'https://www.skillshare.com/',
        'cookie': SKILLSHARE_COOKIE
        }
    )

    if not res.status_code == 200:
        raise Exception('Fetch error, code == {}'.format(res.status_code))

    return res.json()

def get_video_hashids(course_data_list):
	for data in course_data_list:	
		print('*'*89, f'{data = }', '*'*89)
		for s in data['_embedded']['sessions']['_embedded']['sessions']:
			video_id = None
			if 'video_hashed_id' in s and s['video_hashed_id']:
				video_id = s['video_hashed_id'].split(':')[1]

			if not video_id:
				raise Exception('Failed to read video ID from data')
			
			print('*'*89, f'{s = }', '*'*89)


SKILLSHARE_COOKIE = 'device_session_id=27a3a4e6-def6-4b0c-9793-3710d61a2226; accept_language=en-US; show-like-copy=0; YII_CSRF_TOKEN=aUwyNGZnN3Z3M0dPZEtmb1gwZ2tmUzVJek1wN016NE-Tfoi4emi3OxClHgJwG7vyN4vL_rh8as3OlyvmubZodQ%3D%3D; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; __stripe_mid=1436d8bf-5bff-4cf4-a3b3-f4d758287fd307d892; g_state={"i_p":1659938346812,"i_l":1}; __stripe_sid=6449a4ca-13d6-4fd7-9500-d02e7ea9db5d93bad6; ss_hide_default_banner=1665236244.438; PHPSESSID=a55cceac9739a8ab56156f5b3002c06f'
fetch_course_data_by_class_id(course_id=str(1382946907))
for course_id in course_ids_list:
    course_id=course_id['sku']
    print(f'{course_id = }')
    fetch_course_data_by_class_id(course_id=course_id)