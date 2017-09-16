from youtube import YoutubeSearch
from query_set import QUERY_SET, prepare_query_set

'''
tworzenie zapytania i wypisywanie wynikow wyszukiwania
'''

API_KEY='' # podaj swoj klucz API

yt=YoutubeSearch(API_KEY)

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
