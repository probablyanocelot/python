import os
import requests
from lxml import etree
from dotenv import load_dotenv
load_dotenv('.env')

YT_API_KEY = os.getenv('YT_API_KEY')


def yt_vid_name(api_key, id):
    # url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}'
    url = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={YT_API_KEY}').json()
    # url_json = json.loads(url)
    print(url['items'][0]['snippet']['title'])
    # title = url_json['entry']['title']['$t']
    # return title
    # author = json['entry']['author'][0]['name']
