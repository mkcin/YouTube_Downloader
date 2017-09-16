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

    def get_html(self):
        if(self.__finhtml==''):
            return self.__constHtml
        return self.__finhtml


if __name__ == '__main__':
    yt=Youtube('AIzaSyDIYMnZXnQ-P7LYEdNQ5sPwUrru0Isn3Js')
    yt.make_request(order='rating', maxResults='10')
    print (yt.getSearchResults())
