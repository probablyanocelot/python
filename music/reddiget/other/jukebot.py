import pafy
import vlc
import json
import pandas as pd
import keyboard
from icecream import ic
from tabulate import tabulate


# json data from reddi-bot -> pandas dataframe
def get_library():
    df = pd.read_json('data.json', orient='table')
    return(df)


def get_url(library, counter=None):
    # ic(type(library))
    post = library.loc[counter]
    # ic(post)
    domain = post['domain']
    url = post['url']
    return url


# link handling youtube-dl (used in pafy)
# do get_bestquality().url to get the url of the best quality
def get_bestquality(url, watch=False):
    video = pafy.new(url)
    if watch:
        best = video.getbest()
    else:
        best = video.getbestaudio()
    return best


def is_yt(library, counter=None):
    try:
        # ic()
        ic(type(library))
        url = url.replace(r'youtu.be', r'youtube.com/v/')
        url = url.replace(r'watch?v=', 'v/')
        # ic(url)
        ic(type(library))
        # ic()
        test_url = get_bestquality(url)
        # ic(type(library))

        return url
    except ValueError:
        # ic()
        # ic(library)
        library = library.drop(labels=counter, axis=0)
        # ic(library)
        library = library.reset_index(drop=True)
        ic(library)
        # ic()
        ic(type(library))
        return library

# displays current song info in terminal


def song_info(library, counter=None):
    show_info = print(tabulate(
        (
            # metadata_key : metadata_value of current song
            [metadata, library[metadata][counter]]
            for metadata in library), headers=['Song No. ' + str(counter), 'Now Playing'], tablefmt='pretty'))
    return show_info


def song_to_playlist(Instance, playlist, url):
    # player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()

    # adding media to media list
    playlist.add_media(Media)


def main(count):
    library = get_library()

    # player objects
    Instance = vlc.Instance()  # "prefer-insecure"
    media_player = vlc.MediaListPlayer()
    playlist = Instance.media_list_new()

    for url in library['url']:

        try:

            url = url.replace(r'youtu.be/', 'youtube.com/watch?v=')

            if url.split('&amp;')[0]:
                url = url.split('&amp;')[0]

            yt_url = get_bestquality(url).url

            count += 1

            song_to_playlist(Instance, playlist, yt_url)
        except:
            # ic()
            library.drop(labels=count, axis=0)
            # ic()
            library.reset_index(drop=True)
            # ic()
    print(len(playlist))
    print(library)
    media_player.set_media_list(playlist)
    keyboard.add_hotkey(r'ctrl + alt + b', lambda: media_player.previous())
    keyboard.add_hotkey(r'ctrl + alt + n', lambda: media_player.next())
    keyboard.add_hotkey(r'ctrl + alt + space', lambda: media_player.pause())
    media_player.play()
    media_player.play_item_at_index(0)
    keyboard.wait(r'ctrl + alt + q')


if __name__ == '__main__':
    main(0)
