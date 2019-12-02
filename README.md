# imdb_web_crawler

IMDB web crawler

Imdb_web_crawler is a Python program for dealing with [IMDB top 1000](https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating&view=advanced). It can crawl, store and query the top 1000 movies

## Installation

Make sure you have the latest stable version of [python3](https://www.python.org/downloads/release/python-380/).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to IMDB Web Crawler. After cloning run the following command to install all the dependencies.

```bash
cd imdb_web_crawler
pip3 install -r requirements.txt
```

## Usage

```python
python3 imdb.py --help
#optional arguments:
#  -h, --help           show this help message and exit
#  --search SEARCH      search string
#  --director DIRECTOR  search by director name
#  --actor ACTOR        search by actor
#  --rank RANK          search by rank 

python3 imdb.py --search "Spielberg hanks"
# ['Saving Private Ryan', 'Catch Me If You Can', 'Bridge of Spies']
# returns movies associated with hanks and Spielberg

python3 imdb.py --search "spielberg hanks" --rank "27" 
#['Saving Private Ryan']

```
