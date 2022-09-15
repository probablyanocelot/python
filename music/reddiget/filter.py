import getreddit
import json
from .producer import publish

data = getreddit.post_data('hiphopheads', '100')
# urls = getreddit.filter_urls(data, criteria='youtu')
songs = getreddit.filter(data, criteria='youtu')

publish('reddit_songs_gotten', songs)


# print(json.loads(songs))
# print(data)
# for item in urls:


# data = json.dumps(urls)
