from operator import mod
import threading
from types import new_class

from panda.models import Panda
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
        item = Watchable("", "https://tfpdl.se/" + self.link, "", "", "")
        print(item.getLink())
        self.result = getDownloadLink(item)
        temp_panda = Panda.objects.get(search=self.link)
        if temp_panda:
            temp_panda.download_link = self.result.getDownloadLink()
            temp_panda.save()
        else:
            new_panda = Panda(search=self.link,
                              download_link=self.result.getDownloadLink())
            new_panda.save()
