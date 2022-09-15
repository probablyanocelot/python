# uncomment ic() lines for debugging
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


# should probably rename to something like url_tester()
def is_yt(library, counter=None):
    try:
        # ic()
        # ic(type(library))
        url = get_url(library, counter)
        ic(url)
        url = url.replace(r'youtu.be', r'youtube.com/v/')
        url = url.replace(r'watch?v=', 'v/')
        ic(url)
        # ic(type(library))
        # ic()
        test_url = get_besturl(url)
        # ic(type(library))

        return url
    except ValueError:
        # ic()
        # ic(library)
        library = library.drop(labels=counter, axis=0)
        # ic(library)
        library = library.reset_index(drop=True)
        # ic(library)
        # ic()
        # ic(type(library))
        return library


# displays current song info in terminal
def song_info(library, counter=None):
    show_info = print(tabulate(
        (
            # metadata_key : metadata_value of current song
            [metadata, library[metadata][counter]]
            for metadata in library), headers=['Song No. ' + str(counter), 'Now Playing'], tablefmt='pretty'))
    return show_info


def song_to_playlist(url):
    # player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()

    # adding media to media list
    playlist.add_media(Media)


# VLC player
def start_player(media_list):
    # setting media list to the media player
    ic(playlist)
    ic()
    media_player.set_media_list(playlist)
    ic()
    player_controls()
    ic()
    media_player.play()
    ic()
    ic(media_player.is_playing())
    keyboard.wait(r'esc')


def player_controls():
    """
    CURRENTLY BROKEN AFTER FIRST ITERATION OF MAIN()
     - check VLC.py for answer? or maybe incorrectly exited loop?

     - *intentions of mirroring skip_next() for skip_prev() when working, 
            maybe implement doubletap (rewind -> skip_prev)
    """
    keyboard.add_hotkey(
        r'ctrl + shift + b', media_player.previous())
    keyboard.add_hotkey(r'alt + shift + n',
                        media_player.next())


def dj(library, counter):
    for song in library:
        ic()
        # THE BELOW FUNCTION IS NOT CHANGING WITH EACH ITERATION
        song_or_df = media_or_not(library, counter)
        ic()
        print(type(dj))
        counter += 1
        print(counter)


def main(library, counter):
    # localize counter, probably unnecessary
    # counter = counter
    # url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    # ic(type(library))
    library = library
    # ic(type(library))

    # while counter < len(library):
    counter = 0
    dj(library, counter)
    start_player(playlist)


if __name__ == '__main__':
    # player objects
    # can put this in fn to easily create new instance
    Instance = vlc.Instance()  # "prefer-insecure"
    media_player = vlc.MediaListPlayer()
    playlist = Instance.media_list_new()

    # declare here or in body?
    library = get_library()
    counter = 0

    main(library, counter)
