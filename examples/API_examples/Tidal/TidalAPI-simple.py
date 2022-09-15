# pipenv install -e git+https://github.com/tamland/python-tidal.git@0.7.x#egg=tidalapi
import tidalapi
import os

# 0.7.x
session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()
playlist = session.playlist('4261748a-4287-4758-aaab-6d5be3e99e52')
tracks = playlist.tracks()
for track in tracks:
    print(track.name)
