import json
from functools import reduce

import pprint 
pp = pprint.PrettyPrinter(indent=4)

class Indexer:
    """
    Indexer class is repsonsible to create an index for efficient retrieval
    of data 

    attributes:
        self.index = stores the index
    """
    def __init__(self):
        self.index = {}
        self.file_name = "data.json"

    def initialize_index(self):
        """
        Thid function reads the data and creates an index map and stores it in
        self.index
        """
        with open(self.file_name, 'rb') as f:
            try:
                data = json.load(f)
            except:
                data = None

            # print(data["1"])
            # data_ = {"1":data["1"]}
            for dat in data:
                curr = data[dat]
                # print(dat)
                actors = " ".join(curr['actors']).lower()
                actors = actors.split(" ")
                directors = curr["director"].lower()
                directors = directors.split(" ")

                for actor in actors:
                    actor = actor.lower()
                    if actor not in self.index:
                        self.index[actor] = []
                    self.index[actor].append(dat)

                for director in directors:
                    director = director.lower()
                    if director not in self.index:
                        self.index[director] = []
                    self.index[director].append(dat)
        # print(self.index)
    
    def common_movies(self, s):
        """
        this function takes in a string of actor/director names and return a
        list of movies that are common to all of them 

        arguments:
            s: an input string that contains names of actors or directors
        """
        s = s.strip()
        actors = s.split(" ")
        common = []
        for actor in actors:
            common.append(self.index[actor])
        #print(common)
        res = list(reduce(lambda i, j: i & j, (set(x) for x in common)))
        #print(res)
        return res
