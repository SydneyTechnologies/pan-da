class Watchable():
    # this is a class that contains all the necessary
    # information needed to continue the search and download process
    def __init__(self, title, link, description, image):
        self.title = str(title)
        self.link = link
        self.description = description
        self.image = image
        self.downloadLink = ''

    def __str__(self) -> str:
        return self.title

    def getLink(self):
        return self.link

    def updateDownloadLink(self, download_link):
        self.downloadLink = download_link
