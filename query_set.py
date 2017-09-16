'''
wczytywanie kryteriow zapytania
'''
import re

QUERY_SET = {
    'query': '',
    'max_result': '',
    'v_type': '',
    'v_duration': '',
    'v_order': ''
}

def prepare_query_set():
    query = input("what to search:\n")
    if(query == ''):
        query = None
        print("niepoprawny format lub nie podano")
    QUERY_SET['query'] = query

    max_result = input("max results:\n")
    if(re.match(r'^([0-9]+)$', str(max_result))):
        max_result = int(max_result)
    else:
        max_result = None
        print("niepoprawny format lub nie podano")
    QUERY_SET['max_result'] = max_result

    video_type = 'video'
    QUERY_SET['v_type'] = video_type

    v_duration = input("video duration:\n1 - any\n2 - long\n3 - medium\n4 - short\n")
    duration = {
        '1': 'any',
        '2': 'long',
        '3': 'medium',
        '4': 'short' }
    if(re.match(r'^([0-9]+)$', str(v_duration)) and int(v_duration) >= 1 and int(v_duration) <= 4):
        v_duration = duration[v_duration]
    else:
        print("niepoprawny format lub nie podano")
        v_duration = None
    QUERY_SET['v_duration'] = v_duration

    v_order = input("sort by:\n1 - relevance\n2 - upload date\n3 - viewcount\n4 - rating\n")
    order = {
        "1": "relevance",
        "2" : "date",
        "3" : "viewcount",
        "4" : "rating" }
    if(re.match(r'^([0-9]+)$', str(v_order)) and int(v_order) >= 1 and int(v_order) <= 4):
        v_order = order[v_order]
    else:
        print("niepoprawny format lub nie podano")
        v_order = None
    QUERY_SET['v_order'] = v_order

if __name__ == '__main__':
    prepare_query_set()
    print (QUERY_SET)
