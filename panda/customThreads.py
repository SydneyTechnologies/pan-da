import threading
from . watchable import Watchable
from . pandaSearch import getDownloadLink, startSearch


class CustomSearchThread(threading.Thread):
    # this is a custom threading class that would allow multiple
    # requests to made concurrently
    def __init__(self, search):
        super(CustomSearchThread, self).__init__()
        self.search = search
        self.result = False

    def run(self):
        self.result = startSearch(self.search)
        return self.result


class CustomProcessThread(threading.Thread):
    # this is a custom threading class that would allow multiple
    # requests to made concurrently
    def __init__(self, link):
        super(CustomProcessThread, self).__init__()
        self.link = link
        self.result = False

    def run(self):
        item = Watchable("", "https://tfpdl.se/" + self.link, "", "")
        print(item.getLink())
        self.result = getDownloadLink(item)
        return self.result
