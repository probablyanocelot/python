# THIS IS FOR DATA STREAMS IN LOCAL MEMORY

# https://stackoverflow.com/questions/35662828/passing-file-like-objects-to-ctypes-callbacks
import pafy
import vlc
import keyboard
import jukebot as jb  # for testing
import icecream as ic
import ctypes
import io
import sys
import time
import requests


MediaOpenCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(
    ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
MediaReadCb = ctypes.CFUNCTYPE(
    ctypes.c_ssize_t, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_size_t)
MediaSeekCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint64)
MediaCloseCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

stream = None


def media_open_cb(opaque, data_pointer, size_pointer):
    data_pointer.value = opaque
    size_pointer.contents.value = sys.maxsize
    return 0


def media_read_cb(opaque, buffer, length):
    new_data = stream.read(length)
    for i in range(len(new_data)):
        buffer[i] = new_data[i]
    return len(new_data)


def media_seek_cb(opaque, offset):
    stream.seek(offset)
    return 0


def media_close_cb(opaque):
    stream.close()


callbacks = {
    'open': MediaOpenCb(media_open_cb),
    'read': MediaReadCb(media_read_cb),
    'seek': MediaSeekCb(media_seek_cb),
    'close': MediaCloseCb(media_close_cb)
}


def main(path):
    global stream
    stream = open(path, 'rb')
    instance = vlc.Instance('-vvv')
    player = instance.media_player_new()
    media = instance.media_new_callbacks(
        None, callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.byref(ctypes.py_object(stream)))
    player.set_media(media)
    player.play()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Usage: {0} <path>'.format(__file__))
        sys.exit(1)

    main(path)


# MediaOpenCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(
#     ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
# MediaReadCb = ctypes.CFUNCTYPE(
#     ctypes.c_ssize_t, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_size_t)
# MediaSeekCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint64)
# MediaCloseCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)


# def media_open_cb(opaque, data_pointer, size_pointer):
#     data_pointer.contents.value = opaque
#     size_pointer.contents.value = sys.maxsize
#     return 0


# def media_read_cb(opaque, buffer, length):
#     stream = ctypes.cast(opaque, ctypes.POINTER(
#         ctypes.py_object)).contents.value
#     new_data = stream.read(length)
#     for i in range(len(new_data)):
#         buffer[i] = new_data[i]
#     return len(new_data)


# def media_seek_cb(opaque, offset):
#     stream = ctypes.cast(opaque, ctypes.POINTER(
#         ctypes.py_object)).contents.value
#     stream.seek(offset)
#     return 0


# def media_close_cb(opaque):
#     stream = ctypes.cast(opaque, ctypes.POINTER(
#         ctypes.py_object)).contents.value
#     stream.close()


# callbacks = {
#     'open': MediaOpenCb(media_open_cb),
#     'read': MediaReadCb(media_read_cb),
#     'seek': MediaSeekCb(media_seek_cb),
#     'close': MediaCloseCb(media_close_cb)
# }


# def ctypes_main(path):
#     # stream = open(path, 'rb')
#     stream = requests.get(path, stream=True)
#     instance = vlc.Instance()
#     player = instance.media_player_new()
#     media = instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(
#         ctypes.pointer(ctypes.py_object(stream)), ctypes.c_void_p))
#     player.set_media(media)
#     player.play()

#     while True:
#         time.sleep(1)


# def start_player(url, library=None, counter=None):
#     Instance = vlc.Instance("prefer-insecure")
#     player = Instance.media_player_new()
#     # Media = Instance.media_new(url)
#     Media = Instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(
#         ctypes.pointer(ctypes.py_object(url)), ctypes.c_void_p))
#     # Media.get_mrl()
#     player.set_media(Media)
#     player_controls(player)
#     player.play()
#     keyboard.wait('esc')


# def player_controls(player, library=None, counter=None, ):
#     keyboard.add_hotkey(r'ctrl + shift + b', print, args='previous')
#     keyboard.add_hotkey(r'alt + shift + n', print, args='previous')
#     '''
#     keyboard.add_hotkey(r'alt + shift + n', lambda: play_next(player))
#     '''


# if __name__ == '__main__':
#     url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
#     # url = 'http://ab-pr-cf.audio.tidal.com/4cacf116a17313d6496d33e67a40342f_37.mp4?Expires=1642245527&Signature=UC~bJ2lKQmFqbn8K~uR29e9v9MAO51RCfqquvNQAjC~sgOBSN325u8APTvunMZizGLNYtH0HFsOzAn-bKhJfutTPsRBrgYdSYt8kGGABEMqV-qmzADrF~eWYkTxMCJhfa9ryZLxWMYPHCyYxn6Ok7Ura5ZT-KfuoegDT3~6OShNyR7GIAMC3MgbfB5iOK~jErdP9rGduvUjAVb-h0xc0FJEGknGa3HUEtndzhvqH72lecwIPO12KM6j~wiS3N61~VuPQ2zy9rFL8299o09995kiCZBDW3OLGYC3LwxmcCPZp9fabEBvNWnf2V4u0JwtfvQR0cf0uZ9XUqBTim2sPIw__&Key-Pair-Id=APKAIZ3WPBE4R6SP555A'
#     url = jb.get_besturl(url)
#     start_player(url)
#     # ctypes_main(url)
