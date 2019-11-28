from crawler import Crawler
from db import DB


class API:
    """
    The API class contains the crawler and the DB class objects
    Its initializes both the objects and sets the data. It also 
    has a search method that accepts a dictionary of search parameters.
    """
    def __init__(self):
        self.crawler = Crawler()
        self.db = DB()
        if not self.db.is_data_set():
            self.crawler.initialize()
        self.db.read_data()

    def search(self, search_params):
        """
        The search function accepts a dictionary of search parameters
        and returns the results

        args: 
            search_params: dict()
        """
        if self.db.is_data_set():
            return self.db.search(search_params)
        else:
            self.crawler.initialize()
            # return self.db.search(search_params)
