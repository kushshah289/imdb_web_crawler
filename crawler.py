import requests
from bs4 import BeautifulSoup
import io, json


class Crawler:
    def __init__(self):
        """
        The crawler class is responsible to crawl the webpage, parse the html
        and write the data to a temporary file.
        """
        self.json_data = {}


    def get_data(self):
        """
        This function crawls and parses the webpage and stores the data in the
        self.json_data member variable.
        """
        print("Crawling the IMDB website...")
        for i in range(1,1000, 50):
            # print(i)
            url = f"https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start={i}&ref_=adv_nxt";
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            page_data = soup.find_all(class_='lister-item-content')

            for pg in page_data:
                movie_name = pg.find('a').text if pg.find('a') else ""
                genre = pg.find(class_= 'genre').text.strip() if pg.find(class_= 'genre') else "" 
                rank = pg.find(class_='lister-item-index unbold text-primary').text.strip()[:-1] if pg.find(class_='lister-item-index unbold text-primary') else ""
                certificate = pg.find(class_='certificate').text if pg.find(class_='certificate') else ""
                runtime = pg.find(class_='runtime').text if pg.find(class_='runtime') else ""
                rating = pg.find(class_='ratings-imdb-rating').text.strip() if pg.find(class_='ratings-imdb-rating') else ""
                metascore = pg.find(class_='metascore').text.strip() if pg.find(class_='metascore') else ""
                z = pg.find_all('p')
                description = z[1].text.strip() if z[1] else ""
                d_a = z[2].find_all('a')
                director = d_a[0].text
                actors = []
                for d in d_a:
                    actors.append(d.text)
                actors = actors[1:]
                inner_data = {}
                inner_data['movie_name'] = movie_name
                inner_data['genre'] = genre
                inner_data['rank'] = rank
                inner_data['certificate'] = certificate
                inner_data['runtime'] = runtime
                inner_data['rating'] = rating
                inner_data['metascore'] = metascore
                inner_data['description'] = description
                inner_data['director'] = director
                inner_data['actors'] = actors
                self.json_data[rank] = inner_data

    def write_to_file(self):
        """
        This function writes the data to a temporary file so that the subsequest 
        queries do not require to re-crawl the data
        """
        print("Writing to file:")
        with io.open('data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.json_data, ensure_ascii=False))
        self.json_data = {}

    
    def initialize(self):
        self.get_data()
        self.write_to_file()


# crawler = Crawler()