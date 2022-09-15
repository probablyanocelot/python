import pafy
import vlc
import keyboard
import jukebot as jb  # for testing
import icecream as ic


def start_player(url, library=None, counter=None):
    Instance = vlc.Instance("prefer-insecure")
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()
    player.set_media(Media)
    player_controls(player)
    player.play()
    keyboard.wait('esc')


def player_controls(player, library=None, counter=None, ):
    keyboard.add_hotkey(r'ctrl + shift + b', print, args='previous')
    keyboard.add_hotkey(r'alt + shift + n', print, args='previous')
    '''
    keyboard.add_hotkey(r'alt + shift + n', lambda: play_next(player))
    '''


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    url = 'http://ab-pr-cf.audio.tidal.com/4cacf116a17313d6496d33e67a40342f_37.mp4?Expires=1642245527&Signature=UC~bJ2lKQmFqbn8K~uR29e9v9MAO51RCfqquvNQAjC~sgOBSN325u8APTvunMZizGLNYtH0HFsOzAn-bKhJfutTPsRBrgYdSYt8kGGABEMqV-qmzADrF~eWYkTxMCJhfa9ryZLxWMYPHCyYxn6Ok7Ura5ZT-KfuoegDT3~6OShNyR7GIAMC3MgbfB5iOK~jErdP9rGduvUjAVb-h0xc0FJEGknGa3HUEtndzhvqH72lecwIPO12KM6j~wiS3N61~VuPQ2zy9rFL8299o09995kiCZBDW3OLGYC3LwxmcCPZp9fabEBvNWnf2V4u0JwtfvQR0cf0uZ9XUqBTim2sPIw__&Key-Pair-Id=APKAIZ3WPBE4R6SP555A'
    url = jb.get_besturl(url)
    start_player(url)
