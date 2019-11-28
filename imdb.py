import sys
import argparse

from api import API

api = API()

parser = argparse.ArgumentParser()
parser.add_argument("--search",  help="search string")
parser.add_argument("--director",  help="search by director name")
parser.add_argument("--actor",  help="search by actor")
parser.add_argument("--rank",  help="search by rank")

args = parser.parse_args()
search_params = {}

if args.search:
    search_params['search'] = args.search
if args.director:
    search_params['director'] = args.director
if args.actor:
    search_params['actors'] = args.actor
if args.rank:
    search_params['rank'] = args.rank

#api.search(search_params)
print(api.search(search_params))