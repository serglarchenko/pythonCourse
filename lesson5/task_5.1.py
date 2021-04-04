import json
import threading
import requests

file = 'resources/links.txt'
JSON_FILE_PATH = 'resources/result.json'


def list_url():
    with open(file) as file_links:
        return file_links.read().split()


def get_valid_link(url):
    list_result = list()
    try:
        r = requests.get(url)
        s_code = r.status_code
    except Exception:
        s_code = 'null'
    list_result.append({'url': url, 'is_ok': s_code == requests.codes.ok if type(s_code) == int else False,
                        'status_code': s_code})
    with open(JSON_FILE_PATH, 'a') as links_validation:
        json.dump(list_result, links_validation, indent=2)


urls = list_url()
treads = []
for t in urls:
    process = threading.Thread(target=get_valid_link, args=[t])
    process.start()
    treads.append(process)
for proc in treads:
    proc.join()
