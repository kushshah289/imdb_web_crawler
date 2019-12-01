import os
import json
from indexer import Indexer

class DB:
    def __init__(self):
        """
        the DB class stores the data in a variable. This class is also responsible 
        to read the data from the json file, if it exists. It is also able to 
        search for data by a dict.
        """
        self.data = None
        self.file_name = 'data.json'
        self.indexer = Indexer()
        self.read_data()
        

    def read_data(self):
        """
        This function reads data from the json file and stores it in a self.data 
        member variable
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb') as f:
                try:
                    self.data = json.load(f)
                except:
                    self.data = None
            self.indexer.initialize_index()
        else:
            print("file does not exist")
            return None


    def is_data_set(self):
        """
        This function returns bool value if the data is initialized in the member variable
        True: if the data is set
        False: if the data is not set
        """
        if self.data == None:
            return False
        else:
            return True
    

    def search(self, search_params):
        """
        This function takes in a dict of search parameters and returns the movie names of
        all the movies that satisfies the conditions

        Args:
            search_params: dict()
        """
        results = self.data
        for key_ in search_params.keys():
            if key_ == 'rank':
                # results = results[search_params['rank']]
                results = {key : val for key, val in results.items() if search_params['rank'] == val['rank']}
            if key_ == 'director':
                results = {key : val for key, val in results.items() if search_params['director'].lower() in val['director'].lower()}
            if key_ == 'actors':
                results = {key : val for key, val in results.items() if search_params['actors'].lower() in " ".join(val['actors']).lower()}
            # if key_ == 'search':
            #     humans = search_params['search'].split(" ")
            #     for human in humans:
            #         results = {key : val for key, val in results.items() if human.lower() in " ".join(val['actors']).lower() or human.lower() in val['director'].lower()}
            if key_ == 'search':
                res = self.indexer.common_movies(search_params['search'].lower())
                results = {key : val for key, val in results.items() if val['rank'] in res}
        movies = []
        for result in results:
             movies.append(results[result]['movie_name'])
        return movies

