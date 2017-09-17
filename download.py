from youtube import YoutubeSearch
from query_set import QUERY_SET, prepare_query_set
from youtube_dl_user import download
import re
from config import API_KEY, DEST_PATH
import os

'''
tworzenie zapytania i wypisywanie wynikow wyszukiwania
'''

yt=YoutubeSearch(API_KEY)

what = input('1 - video\n2 - music\n')
if(what == '2'):
    what = 'music'
else:
    what = 'video'

prepare_query_set()
# print (QUERY_SET)

yt.make_request(
    q = QUERY_SET['query'],
    maxResults = QUERY_SET['max_result'],
    type = QUERY_SET['v_type'],
    videoDuration = QUERY_SET['v_duration'],
    order = QUERY_SET['v_order'] )

# print(yt.get_html())
# print(yt.get_search_results())
yt.print_search_results_readable()

if(what == 'music'):
    choice = input('choose one or more results (divide with \" \"):\n')
    choice = list(choice.strip())
    videoLinks=[]
    # print (choice)
    for ch in choice:
        if(ch != ' '):
            if(not (re.match(r'^([0-9]+)$', str(ch)) and int(ch) >= 1 and int(ch) <= len(yt.get_search_results()['items']))):
                continue
            else:
                videoLink=yt.get_nth_link(int(ch)-1)
                videoLinks.append(videoLink)
    download(videoLinks, 'music')
else:
    choice = 0
    choice = input('number of video:\n')
    if(not (re.match(r'^([0-9]+)$', str(choice)) and int(choice) >= 1 and int(choice) <= len(yt.get_search_results()['items']))):
        choice=1
    # print(yt.get_search_results())
    videoLink=yt.get_nth_link(int(choice)-1)
    download([videoLink], 'video')
