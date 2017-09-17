'''
Klasa Youtube pozwala na wyszukiwanie w yt za pomoca ich api
'''
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

import requests
import json
import youtube_dl

class YoutubeSearch:

    def __init__(self, apikey):
        self.__apiKey = apikey
        self.__constHtml = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
        self.__finhtml = ''
        self.__searchResults = {}
        self.__links=[]

    def __repr__(self):
        return ("Youtube({})".format(self.__apiKey))

    def __str__(self):
        return ("Youtube - key = {}".format(self.__apiKey))

    @staticmethod
    def headering(html, headers):
        for header in headers:
            html += '&'
            html += header + "="
            html += headers[header]
        return html

    @staticmethod
    def remove_empty_kwargs(**kwargs):
        good_kwargs = {}
        if kwargs is not None:
            try:
                for key, value in kwargs.iteritems():
                    if value:
                        good_kwargs[key] = value
            except:
                for key, value in kwargs.items():
                    if value:
                        good_kwargs[key] = value

        return good_kwargs

    def make_request(self, **kwargs):
        kwargs = self.remove_empty_kwargs(**kwargs)
        kwargs['key'] = self.__apiKey
        self.__finhtml = self.headering(self.__constHtml, kwargs)
        response = urlopen(self.__finhtml).read().decode("utf-8")
        self.__searchResults = json.loads(response)


    def get_search_results(self):
        return self.__searchResults

    def print_search_results_readable(self):
        count=1
        for item in self.get_search_results()['items']:
            try:
                print(count)
                count+=1
                print(item["snippet"]["title"])
                print(item["snippet"]["channelTitle"])
                print("DESCRIPTION: " + item["snippet"]["description"])
                videoLink = "https://www.youtube.com/watch?v="+item["id"]["videoId"]
                self.__links.append(videoLink)
                # print(item["id"]["videoId"])
                print(videoLink)
                print()
            except Exception as exc:
                print(str(exc))

    def get_nth_link(self, n):
        return self.__links[n]

    def get_html(self):
        if(self.__finhtml==''):
            return self.__constHtml
        return self.__finhtml


if __name__ == '__main__':
    yt=YoutubeSearch('') # podaj klucz api od google
    yt.make_request(order='rating', maxResults='10') # podaj zapytania(**kwargs)
    print (json.dumps(yt.get_search_results(), indent=2))
    yt.print_search_results_readable()
