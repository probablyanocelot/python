import pafy
import vlc
import json
import pandas as pd
import keyboard
from icecream import ic
from tabulate import tabulate
import ctypes
import io
import sys
import time

import vlc

MediaOpenCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(
    ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
MediaReadCb = ctypes.CFUNCTYPE(
    ctypes.c_ssize_t, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_size_t)
MediaSeekCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint64)
MediaCloseCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)


def media_open_cb(opaque, data_pointer, size_pointer):
    data_pointer.contents.value = opaque
    size_pointer.contents.value = sys.maxsize
    return 0


def media_read_cb(opaque, buffer, length):
    stream = ctypes.cast(opaque, ctypes.POINTER(
        ctypes.py_object)).contents.value
    new_data = stream.read(length)
    for i in range(len(new_data)):
        buffer[i] = new_data[i]
    return len(new_data)


def media_seek_cb(opaque, offset):
    stream = ctypes.cast(opaque, ctypes.POINTER(
        ctypes.py_object)).contents.value
    stream.seek(offset)
    return 0


def media_close_cb(opaque):
    stream = ctypes.cast(opaque, ctypes.POINTER(
        ctypes.py_object)).contents.value
    stream.close()


callbacks = {
    'open': MediaOpenCb(media_open_cb),
    'read': MediaReadCb(media_read_cb),
    'seek': MediaSeekCb(media_seek_cb),
    'close': MediaCloseCb(media_close_cb)
}


def ctypes_main(path):
    stream = open(path, 'rb')
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(
        ctypes.pointer(ctypes.py_object(stream)), ctypes.c_void_p))
    player.set_media(media)
    player.play()

    while True:
        time.sleep(1)

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
def get_besturl(url):
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    return playurl


def is_yt(library, counter=None):
    try:
        # ic()
        ic(type(library))
        url = url.replace(r'youtu.be', r'youtube.com/v/')
        url = url.replace(r'watch?v=', 'v/')
        # ic(url)
        ic(type(library))
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
    # Media = Instance.media_new(url)
    Media = Instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(
        ctypes.pointer(ctypes.py_object(url)), ctypes.c_void_p))

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

            yt_url = get_besturl(url)

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
    media_player.play()
    media_player.play_item_at_index(0)
    keyboard.wait(r'esc')


if __name__ == '__main__':
    main(0)


'''
CTYPES if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Usage: {0} <path>'.format(__file__))
        sys.exit(1)

    main(path)
'''
