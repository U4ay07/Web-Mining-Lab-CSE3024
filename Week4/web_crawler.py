from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from urllib.error import HTTPError
from http.client import InvalidURL
from ssl import _create_unverified_context

class AnchorParser(HTMLParser):
    def __init__(self, baseURL = ""):
        HTMLParser.__init__(self)
        self.pageLinks = set()
        self.baseURL = baseURL

    def getLinks(self):
        return self.pageLinks

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for(attribute, value) in attrs:
                if attribute == "href":
                    absoluteUrl = urljoin(self.baseURL, value)
                    if urlparse(absoluteUrl).scheme in ["http", "https"]:
                        self.pageLinks.add(absoluteUrl)


class MyWebCrawler(object):

    def __init__(self, url, maxCrawl=10):
        self.visited = set() # To track all visited urls
        self.starterUrl = url
        self.max = maxCrawl

    def crawl(self):
        urlsToParse = {self.starterUrl}
        while(len(urlsToParse) > 0 and len(self.visited) < self.max):
            nextUrl = urlsToParse.pop()
            if nextUrl not in self.visited:
                self.visited.add(nextUrl)
                print("Crawling: {}".format(nextUrl))
                urlsToParse |= self.parse(nextUrl)

    def parse(self, url):
        try:
            htmlContent = urlopen(url, context=_create_unverified_context()).read().decode()
            parser = AnchorParser(url)
            parser.feed(htmlContent)
            return parser.getLinks()
        except (HTTPError, InvalidURL, UnicodeDecodeError):
            print("Failed: {}".format(url))
            return set()

    def getVisited(self):
        return self.visited


if __name__ == "__main__":
    crawler = MyWebCrawler("http://www.vit.ac.in", maxCrawl=10)
    crawler.crawl()
    print("\nThe following sites were visited:\n{}".format(crawler.getVisited()))
